import { CommonModule } from "@angular/common";
import { NgModule } from "@angular/core";
import { RouterModule } from "@angular/router";

import { NgZorroCustomModule } from "../utils/ng-zorro-custom.module";

import { AsideComponent } from "./aside/aside.component";
import { MainComponent } from "./main/main.component";
import { NavComponent } from "./nav/nav.component";

@NgModule({
  declarations: [NavComponent, MainComponent, AsideComponent],
  imports: [CommonModule, RouterModule, NgZorroCustomModule],
  exports: [MainComponent],
})
export class LayoutModule {}
