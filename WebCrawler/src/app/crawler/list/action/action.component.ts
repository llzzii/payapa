import { Component, EventEmitter, Input, OnInit, Output } from "@angular/core";
import { FormArray, FormBuilder, FormGroup, Validators } from "@angular/forms";
import { NzMessageService } from "ng-zorro-antd/message";
import { NzModalService } from "ng-zorro-antd/modal";
import { CrawlerService } from "src/app/service/crawler.service";

import { DataConfigComponent } from "../data-config/data-config.component";

@Component({
  selector: "app-action",
  templateUrl: "./action.component.html",
  styleUrls: ["./action.component.less"],
})
export class ActionComponent implements OnInit {
  get headerList(): FormArray {
    return this.updateForm.get("headerList") as FormArray;
  }
  get bodyList(): FormArray {
    return this.updateForm.get("bodyList") as FormArray;
  }
  get paramList(): FormArray {
    return this.updateForm.get("paramList") as FormArray;
  }
  set paramList(val) {}
  set bodyList(val) {}
  set headerList(val) {}
  @Output() getProjectDatas = new EventEmitter();
  @Input() rowData;
  updateForm: FormGroup;
  dataConfigForm: FormGroup;
  constructor(
    private crawlerService: CrawlerService,
    private fb: FormBuilder,
    private message: NzMessageService,
    private modalService: NzModalService
  ) {
    this.updateForm = this.fb.group({
      name: [
        "",
        [
          Validators.required,
          Validators.pattern("^[A-Za-z0-9]+$"),
          Validators.maxLength(36),
          Validators.minLength(3),
        ],
      ],
      url: ["", [Validators.required]],
      method: ["", [Validators.required]],
      headerList: this.fb.array([]),
      bodyList: this.fb.array([]),
      paramList: this.fb.array([]),
    });
  }

  // 新增弹窗
  update(tpl) {
    const that = this;
    if (that.rowData) {
      that.updateForm.get("name").setValue(that.rowData["name"]);
      that.updateForm.get("url").setValue(that.rowData["url"]);
      that.updateForm.get("method").setValue(that.rowData["method"]);
      //   that.addForm.get("headerList").setValue(that.rowData["headerList"]);
      //   that.addForm.get("bodyList").setValue(that.rowData["bodyList"]);
      //   that.addForm.get("paramList").setValue(that.rowData["paramList"]);
      //   that.headerList = that.rowData["headerList"];
      //   that.bodyList = that.rowData["bodyList"];
      //   that.paramList = that.rowData["paramList"];
      that.rowData["headerList"].forEach((element) => {
        that.headerList.push(
          this.fb.group({
            keys: [element["keys"]],
            val: [element["val"]],
            type: [element["type"]],
          })
        );
      });
      that.rowData["bodyList"].forEach((element) => {
        that.bodyList.push(
          this.fb.group({
            keys: [element["keys"]],
            type: [element["type"]],
            val: [element["val"]],
          })
        );
      });
      that.rowData["paramList"].forEach((element) => {
        that.paramList.push(
          this.fb.group({
            keys: [element["keys"]],
            val: [element["val"]],
            type: [element["type"]],
          })
        );
      });
    }
    const model = this.modalService.create({
      nzTitle: "编辑爬虫",
      nzContent: tpl,
      nzMaskClosable: false,
      nzWidth: 700,
      nzOnOk() {
        let isV = that.submitForm();
        return isV;
      },
      nzOnCancel() {},
    });
  }

  delete() {
    const that = this;
    const model = this.modalService.confirm({
      nzTitle: "删除爬虫",
      nzContent: "确认删除该项目吗",
      nzMaskClosable: false,
      nzWidth: 500,
      nzOnOk() {
        let mid = that.message.loading("正在删除中", {
          nzDuration: 0,
        }).messageId;
        that.crawlerService.deleteProject(that.rowData._id).subscribe(
          (res) => {
            that.getProjectDatas.emit();
            that.message.success("删除操作成功！");
            that.message.remove(mid);
          },
          (err) => {
            that.message.error("删除操作失败！");
            that.message.remove(mid);
          }
        );
      },
      nzOnCancel() {},
    });
  }

  // 数据提交
  submitForm(id = null) {
    for (const i in this.updateForm.controls) {
      this.updateForm.controls[i].markAsDirty();
      this.updateForm.controls[i].updateValueAndValidity();
    }
    if (this.updateForm.status !== "VALID") {
      return false;
    }
    let data: any = {};
    for (const i in this.updateForm.controls) {
      if (i) {
        let value = this.updateForm.controls[i].value;
        data[i] = typeof value === "string" ? value.trim() : value;
      }
    }
    console.log(data);
    this.updateData(data);
  }

  // 新增
  updateData(data) {
    let mid = this.message.loading("正在更新中", {
      nzDuration: 0,
    }).messageId;
    this.crawlerService.updateProject(this.rowData._id, data).subscribe(
      (res) => {
        this.getProjectDatas.emit();
        this.message.success("更新操作成功！");
        this.message.remove(mid);
      },
      (err) => {
        this.message.error("更新操作失败！");
        this.message.remove(mid);
      }
    );
  }

  addField(e?: MouseEvent, item = "headerList"): void {
    if (e) {
      e.preventDefault();
    }
    this[item].push(this.createAddrItem());
  }
  removeField(i: number, item = "headerList"): void {
    // console.log(i);
    if (this[item].length > 1) {
      this[item].removeAt(i); // 根据索引移除对应的表单
    }
  }
  action() {
    let mid = this.message.loading("正在启动中", {
      nzDuration: 0,
    }).messageId;
    this.crawlerService.projectAction(this.rowData._id).subscribe(
      (res) => {
        this.getProjectDatas.emit();
        this.message.success("启动操作成功！");
        this.message.remove(mid);
      },
      (err) => {
        this.message.error("启动操作失败！");
        this.message.remove(mid);
      }
    );
  }
  dataConfig() {
    const modal = this.modalService.create({
      nzTitle: "数据配置",
      nzContent: DataConfigComponent,
      nzWidth: 900,
      nzComponentParams: {
        rowData: this.rowData,
      },
      nzOnOk: () => {
        let isValid: boolean = modal.getContentComponent().submitForm();

        modal.getContentComponent().createSucceed.subscribe(() => {
          this.getProjectDatas.emit();
        });

        return isValid;
      },
    });
  }
  ngOnInit(): void {}
  private createAddrItem(): FormGroup {
    return this.fb.group({
      keys: [null, [Validators.required]],
      val: [null, [Validators.required]],
      type: [null, [Validators.required]],
    });
  }
}
