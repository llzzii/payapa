import { CommonModule } from "@angular/common";
import { NgModule } from "@angular/core";
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { RouterModule, Routes } from "@angular/router";

import { CrawlerService } from "../service/crawler.service";
import { NgZorroCustomModule } from "../utils/ng-zorro-custom.module";

import { ListComponent } from "./list/list.component";
import { CreateComponent } from "./list/create/create.component";
import { ActionComponent } from "./list/action/action.component";
import { DataConfigComponent } from "./list/data-config/data-config.component";
import { DataListComponent } from "./data-list/data-list.component";

const routes: Routes = [
  {
    path: "list",
    data: {},
    children: [{ path: "", component: ListComponent }],
  },
  {
    path: "data",
    data: {},
    children: [{ path: "", component: DataListComponent }],
  },
  { path: "", redirectTo: "list", pathMatch: "full" },
];

@NgModule({
  declarations: [
    ListComponent,
    CreateComponent,
    ActionComponent,
    DataConfigComponent,
    DataListComponent,
  ],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    NgZorroCustomModule,
    RouterModule.forChild(routes),
  ],
  providers: [CrawlerService],
})
export class CrawlerModule {}
