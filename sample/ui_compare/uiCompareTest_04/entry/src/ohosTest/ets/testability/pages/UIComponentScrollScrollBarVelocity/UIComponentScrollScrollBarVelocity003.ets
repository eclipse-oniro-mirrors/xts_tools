/*
 * Copyright (c) 2025 Shenzhen Kaihong Digital Industry Development Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

@Entry
@Component
struct UIComponentScrollScrollBarVelocity003 {
  @State message: string = 'Hello'
  scroller1: Scroller = new Scroller()
  scroller2: Scroller = new Scroller()
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  build() {
    Column() {
      Text(this.message)
        .fontSize(20)
        .fontColor(Color.Blue)
        .margin({ top: 20 })
        .key('UIComponentScrollScrollBarVelocity003_001')
      Stack({ alignContent: Alignment.TopStart }) {
        Column() {
          Text('friction(0)')
            .fontSize(20)
          Scroll(this.scroller1) {
            Row() {
              ForEach(this.arr, (item: number) => {
                Text(item.toString())
                  .width('40%')
                  .height(150)
                  .backgroundColor(0xFFFFFF)
                  .borderRadius(15)
                  .fontSize(16)
                  .textAlign(TextAlign.Center)
                  .margin({ top: 10 })
              }, (item: string) => item)
            }
          }
          .scrollBar(BarState.On)
          .scrollable(ScrollDirection.Horizontal)
          .scrollBarColor(Color.Blue)
          .initialOffset({ xOffset: 450 })
          Text('friction(2)')
            .fontSize(20)
          Scroll(this.scroller2) {
            Row() {
              ForEach(this.arr, (item: number) => {
                Text(item.toString())
                  .width('40%')
                  .height(150)
                  .backgroundColor(0xFFFFFF)
                  .borderRadius(15)
                  .fontSize(16)
                  .textAlign(TextAlign.Center)
                  .margin({ top: 10 })
              }, (item: string) => item)
            }
          }
          .scrollBar(BarState.On)
          .scrollable(ScrollDirection.Horizontal)
          .scrollBarColor(Color.Blue)
          .initialOffset({ xOffset: 450 })
          .friction(2)
        }

        Button('fling 1000.5')
          .id('scroll')
          .height('5%')
          .stateEffect(true)
          .onClick(() => {
            this.scroller1.fling(1000.5)
            this.scroller2.fling(1000.5)
          })
      }
      .backgroundColor(0xDCDCDC)
      .width('100%')
      .height('100%')
    }
  }
}