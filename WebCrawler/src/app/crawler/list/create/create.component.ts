import { Component, EventEmitter, OnInit, Output } from "@angular/core";
import { FormArray, FormBuilder, FormGroup, Validators } from "@angular/forms";
import { NzMessageService } from "ng-zorro-antd/message";
import { NzModalService } from "ng-zorro-antd/modal";
import { CrawlerService } from "src/app/service/crawler.service";

@Component({
  selector: "app-create",
  templateUrl: "./create.component.html",
  styleUrls: ["./create.component.less"],
})
export class CreateComponent implements OnInit {
  get headerList(): FormArray {
    return this.addForm.get("headerList") as FormArray;
  }
  get bodyList(): FormArray {
    return this.addForm.get("bodyList") as FormArray;
  }
  get paramList(): FormArray {
    return this.addForm.get("paramList") as FormArray;
  }
  @Output() getProjectDatas = new EventEmitter();
  addForm: FormGroup;

  constructor(
    private crawlerService: CrawlerService,
    private fb: FormBuilder,
    private message: NzMessageService,
    private modalService: NzModalService
  ) {
    this.addForm = this.fb.group({
      name: [
        null,
        [
          Validators.required,
          Validators.pattern("^[A-Za-z]+$"),
          Validators.maxLength(36),
          Validators.minLength(3),
        ],
      ],
      url: ["", [Validators.required]],
      method: ["GET", [Validators.required]],
      headerList: this.fb.array([
        this.fb.group({
          keys: [null],
          type: ["String"],
          val: [null],
        }),
      ]),
      bodyList: this.fb.array([
        this.fb.group({
          keys: [null],
          type: ["String"],
          val: [null],
        }),
      ]),
      paramList: this.fb.array([
        this.fb.group({
          keys: [null],
          val: [null],
          type: ["String"],
        }),
      ]),
    });
  }

  // 新增弹窗
  add(tpl) {
    const that = this;
    const model = this.modalService.create({
      nzTitle: "新建爬虫",
      nzContent: tpl,
      nzMaskClosable: false,
      nzWidth: 700,
      nzOnOk() {
        let isV = that.submitForm();
        return isV;
      },
      nzOnCancel() {},
    });
    model.afterOpen.subscribe(() => {
      that.addForm = this.fb.group({
        name: [
          null,
          [
            Validators.required,
            Validators.pattern("^[\u4e00-\u9fa5A-Za-z0-9\\-]+$"),
            Validators.maxLength(36),
            Validators.minLength(3),
          ],
        ],
        url: ["", [Validators.required]],
        method: ["GET", [Validators.required]],
        headerList: this.fb.array([
          this.fb.group({
            keys: [null],
            type: ["String"],
            val: [null],
          }),
        ]),
        bodyList: this.fb.array([
          this.fb.group({
            keys: [null],
            type: ["String"],
            val: [null],
          }),
        ]),
        paramList: this.fb.array([
          this.fb.group({
            keys: [null],
            val: [null],
            type: ["String"],
          }),
        ]),
      });
    });
  }

  // 数据提交
  submitForm(id = null) {
    for (const i in this.addForm.controls) {
      this.addForm.controls[i].markAsDirty();
      this.addForm.controls[i].updateValueAndValidity();
    }
    if (this.addForm.status !== "VALID") {
      return false;
    }
    let data: any = {};
    for (const i in this.addForm.controls) {
      if (i) {
        let value = this.addForm.controls[i].value;
        data[i] = typeof value === "string" ? value.trim() : value;
      }
    }
    console.log(data);
    this.create(data);
  }

  // 新增
  create(data) {
    let mid = this.message.loading("正在创建中", {
      nzDuration: 0,
    }).messageId;
    this.crawlerService.addProject(data).subscribe(
      (res) => {
        this.getProjectDatas.emit();
        this.message.success("创建操作成功！");
        this.message.remove(mid);
      },
      (err) => {
        this.message.error("创建操作失败！");
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

  ngOnInit(): void {}
  private createAddrItem(): FormGroup {
    return this.fb.group({
      keys: [null, [Validators.required]],
      type: ["String", [Validators.required]],
      val: [null, [Validators.required]],
    });
  }
}
