import { Component, OnInit } from "@angular/core";
import { FormArray, FormBuilder, FormGroup, Validators } from "@angular/forms";
import { NzMessageService } from "ng-zorro-antd/message";
import { NzModalService } from "ng-zorro-antd/modal";

import { CrawlerService } from "../../service/crawler.service";

@Component({
  selector: "app-data-list",
  templateUrl: "./data-list.component.html",
  styleUrls: ["./data-list.component.less"],
})
export class DataListComponent implements OnInit {
  displayData = []; // 获取实例内容
  dataSet = []; // 获取实例内容
  // 分页
  current = 1;
  pageSize = 10;
  totalCount = 0;
  isLoading = true;
  addForm: FormGroup;
  projectId = "";
  projectDatas = [];
  headerList = [];
  constructor(
    private crawlerService: CrawlerService,
    private fb: FormBuilder,
    private message: NzMessageService,
    private modalService: NzModalService
  ) {}
  getProjectDatas(reset = false) {
    this.isLoading = true;

    if (reset) {
      this.current = 1;
    }

    this.displayData = [];
    this.crawlerService
      .listByProject(this.projectId, this.current - 1, this.pageSize)
      .subscribe(
        (res) => {
          this.isLoading = false;
          this.dataSet = res.data;
          this.displayData = res.data;
          this.totalCount = res.total;

          if (this.dataSet.length > 0) {
            this.headerList = [];
            for (let key in this.dataSet[0]) {
              this.headerList.push(key);
            }
          }
        },
        (err) => {
          this.isLoading = false;
        }
      );
  }

  listDb() {
    this.crawlerService.listDb().subscribe(
      (res) => {
        this.isLoading = false;
        this.projectDatas = res.data;
        if (this.projectDatas.length > 0) {
          this.projectDatas = this.projectDatas.filter((e) => {
            return e.endsWith("_data");
          });
          this.projectId = res.data[0];
          this.getProjectDatas();
        }
      },
      (err) => {
        this.isLoading = false;
      }
    );
  }
  ngOnInit(): void {
    this.listDb();
  }
}
