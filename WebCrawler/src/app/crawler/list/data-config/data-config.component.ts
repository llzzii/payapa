import { Component, EventEmitter, Input, OnInit, Output } from "@angular/core";
import { FormArray, FormBuilder, FormGroup, Validators } from "@angular/forms";
import { NzMessageService } from "ng-zorro-antd/message";
import { NzModalService } from "ng-zorro-antd/modal";
import { CrawlerService } from "src/app/service/crawler.service";

@Component({
  selector: "app-data-config",
  templateUrl: "./data-config.component.html",
  styleUrls: ["./data-config.component.less"],
})
export class DataConfigComponent implements OnInit {
  @Input() rowData;
  @Output() createSucceed = new EventEmitter();
  dataConfigForm: FormGroup;
  fieldList: FormArray;
  id = "";
  constructor(
    private crawlerService: CrawlerService,
    private fb: FormBuilder,
    private message: NzMessageService,
    private modalService: NzModalService
  ) {
    this.dataConfigForm = this.fb.group({
      dataLocation: this.fb.array([]),
      fieldsList: this.fb.array([]),
    });
  }
  get dataLocation(): FormArray {
    return this.dataConfigForm.get("dataLocation") as FormArray;
  }
  get fieldsList(): FormArray {
    return this.dataConfigForm.get("fieldsList") as FormArray;
  }
  field(val: FormGroup): FormArray {
    return val.get("field") as FormArray;
  }

  addField(e?: MouseEvent, item = "dataLocation"): void {
    if (e) {
      e.preventDefault();
    }
    this[item].push(this.createAddrItem());
  }
  removeField(i: number, item = "dataLocation"): void {
    // console.log(i);
    if (this[item].length > 1) {
      this[item].removeAt(i); // 根据索引移除对应的表单
    }
  }
  addField3(e: MouseEvent, i): void {
    if (e) {
      e.preventDefault();
    }
    let fields = this["fieldsList"].controls[i].get("field") as FormArray;
    fields.push(this.createAddrItem());
  }

  removeField3(i: number, j): void {
    let fields = this["fieldsList"].controls[j].get("field") as FormArray;
    // console.log(i);
    if (fields.length > 1) {
      fields.removeAt(i); // 根据索引移除对应的表单
    }
  }
  addField1(e?: MouseEvent, item = "fieldsList"): void {
    if (e) {
      e.preventDefault();
    }
    this[item].push(this.createFildItem());
  }

  // 数据提交
  submitForm(id = null) {
    for (const i in this.dataConfigForm.controls) {
      this.dataConfigForm.controls[i].markAsDirty();
      this.dataConfigForm.controls[i].updateValueAndValidity();
    }
    if (this.dataConfigForm.status !== "VALID") {
      return false;
    }
    let data: any = {};
    for (const i in this.dataConfigForm.controls) {
      if (i) {
        let value = this.dataConfigForm.controls[i].value;
        data[i] = typeof value === "string" ? value.trim() : value;
      }
    }
    console.log(data);
    data = Object.assign(this.rowData, data);
    delete data["_id"];
    console.log(data);

    this.updateData(data);
  }
  updateData(data) {
    let mid = this.message.loading("正在更新中", {
      nzDuration: 0,
    }).messageId;
    this.crawlerService.updateProject(this.id, data).subscribe(
      (res) => {
        this.createSucceed.emit();
        this.message.success("更新操作成功！");
        this.message.remove(mid);
      },
      (err) => {
        this.message.error("更新操作失败！");
        this.message.remove(mid);
      }
    );
  }
  ngOnInit(): void {
    if (this.rowData) {
      this.id = this.rowData._id;
      this.rowData["dataLocation"] &&
        this.rowData["dataLocation"].forEach((element) => {
          this.dataLocation.push(
            this.fb.group({
              val: [element["val"]],
            })
          );
        });
      this.rowData["fieldsList"] &&
        this.rowData["fieldsList"].forEach((element) => {
          let fieldList = this.fb.array([]);
          element["field"].forEach((ele) => {
            fieldList.push(
              this.fb.group({
                val: [ele["val"]],
              })
            );
          });
          this.fieldsList.push(
            this.fb.group({
              type: [element["type"]],
              field: fieldList,
            })
          );
        });
    }
  }
  private createAddrItem(): FormGroup {
    return this.fb.group({
      val: [""],
    });
  }
  private createFildItem(): FormGroup {
    return this.fb.group({
      type: ["String"],
      field: this.fb.array([
        this.fb.group({
          val: [""],
        }),
      ]),
    });
  }
}
