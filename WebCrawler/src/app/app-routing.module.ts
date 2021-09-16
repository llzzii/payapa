import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { MainComponent } from "./layout/main/main.component";

const routes: Routes = [
  {
    path: "",
    component: MainComponent,
    children: [
      {
        path: "crawler",
        loadChildren: () =>
          import("./crawler/crawler.module").then((m) => m.CrawlerModule),
        data: {
          breadcrumb: "概览",
        },
        // canActivate: [AuthService],
      },

      { path: "", redirectTo: "/crawler", pathMatch: "full" },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
