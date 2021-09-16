import { AfterViewInit, Component, ElementRef, OnInit } from "@angular/core";

@Component({
  selector: "app-main",
  templateUrl: "./main.component.html",
  styleUrls: ["./main.component.less"],
})
export class MainComponent implements AfterViewInit {
  mainHeight: number;
  constructor(private elementRef: ElementRef) {}
  getMainHeight(): number {
    const pageMain =
      this.elementRef.nativeElement.querySelector("#page-main") || {};
    const winH = window.innerHeight,
      mainOffset = pageMain.offsetTop;
    let mainH = winH - (mainOffset || 0);
    mainH = mainH <= 0 ? 1 : mainH;
    return mainH;
  }
  ngAfterViewInit(): void {
    setTimeout(() => {
      this.mainHeight = this.getMainHeight();
    });
  }
}
