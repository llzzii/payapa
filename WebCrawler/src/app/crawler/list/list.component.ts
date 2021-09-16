import { Component, OnInit } from "@angular/core";
import { FormArray, FormBuilder, FormGroup, Validators } from "@angular/forms";
import { NzMessageService } from "ng-zorro-antd/message";
import { NzModalService } from "ng-zorro-antd/modal";

import { CrawlerService } from "../../service/crawler.service";

@Component({
  selector: "app-list",
  templateUrl: "./list.component.html",
  styleUrls: ["./list.component.less"],
})
export class ListComponent implements OnInit {
  displayData = []; // 获取实例内容
  dataSet = []; // 获取实例内容
  // 分页
  current = 1;
  pageSize = 10;
  totalCount = 0;
  isLoading = true;
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
          val: [null],
        }),
      ]),
      bodyList: this.fb.array([
        this.fb.group({
          keys: [null],
          val: [null],
        }),
      ]),
      paramList: this.fb.array([
        this.fb.group({
          keys: [null],
          val: [null],
        }),
      ]),
    });
  }
  getProjectDatas(reset = false) {
    this.isLoading = true;

    if (reset) {
      this.current = 1;
    }

    this.displayData = [];
    this.crawlerService
      .getProjectDatas(this.current - 1, this.pageSize)
      .subscribe(
        (res) => {
          this.isLoading = false;
          this.dataSet = res.data;
          this.displayData = res.data;
          this.totalCount = res.total;
        },
        (err) => {
          this.isLoading = false;
        }
      );
  }
  ngOnInit(): void {
    this.getProjectDatas();
  }

  
}
