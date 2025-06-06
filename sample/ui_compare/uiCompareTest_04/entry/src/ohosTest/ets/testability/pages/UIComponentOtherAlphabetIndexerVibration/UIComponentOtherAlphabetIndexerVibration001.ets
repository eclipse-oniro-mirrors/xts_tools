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
struct UIComponentOtherAlphabetIndexerVibration001 {
  @State message: string = 'Hello'
  private arrayA: string[] = ['安']
  private arrayB: string[] = ['卜', '白', '包', '毕', '丙']
  private arrayC: string[] = ['曹', '成', '陈', '催']
  private arrayL: string[] = ['刘', '李', '楼', '梁', '雷', '吕', '柳', '卢']
  private value: string[] = ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z']

  build() {
    Column() {
      Text(this.message)
        .fontSize(20)
        .fontColor(Color.Blue)
        .height('10%')
        .margin({ top: 20 })
        .key('UIComponentOtherAlphabetIndexerVibration001_001')

      Stack({ alignContent: Alignment.Start }) {
        Row() {
          List({ space: 20, initialIndex: 0 }) {
            ForEach(this.arrayA, (item: string) => {
              ListItem() {
                Text(item)
                  .width('80%')
                  .height(10)
                  .fontSize(30)
                  .textAlign(TextAlign.Center)
              }
            }, (item: string) => item)

            ForEach(this.arrayB, (item: string) => {
              ListItem() {
                Text(item)
                  .width('80%')
                  .height(10)
                  .fontSize(30)
                  .textAlign(TextAlign.Center)
              }
            }, (item: string) => item)

            ForEach(this.arrayC, (item: string) => {
              ListItem() {
                Text(item)
                  .width('80%')
                  .height(10)
                  .fontSize(30)
                  .textAlign(TextAlign.Center)
              }
            }, (item: string) => item)

            ForEach(this.arrayL, (item: string) => {
              ListItem() {
                Text(item)
                  .width('80%')
                  .height(10)
                  .fontSize(30)
                  .textAlign(TextAlign.Center)
              }
            }, (item: string) => item)
          }
          .width('50%')
          .height('100%')

          AlphabetIndexer({ arrayValue: this.value, selected: 0 })
            .enableHapticFeedback(true)
            .selectedColor(0xFFFFFF)
            .popupColor(0xFFFAF0)
            .selectedBackgroundColor(0xCCCCCC)
            .popupBackground(0xD2B48C)
            .usingPopup(true)
            .selectedFont({ size: 16, weight: FontWeight.Bolder })
            .popupFont({ size: 30, weight: FontWeight.Bolder })
            .itemSize(10)
            .alignStyle(IndexerAlign.Left)
            .popupItemBorderRadius(24)
            .itemBorderRadius(14)
            .popupBackgroundBlurStyle(BlurStyle.NONE)
            .popupTitleBackground(0xCCCCCC)
            .popupSelectedColor(0x00FF00)
            .popupUnselectedColor(0x0000FF)
            .popupItemFont({ size: 30, style: FontStyle.Normal })
            .popupItemBackgroundColor(0xCCCCCC)
            .onSelect((index: number) => {
              console.info(this.value[index] + ' Selected!')
            })
            .onRequestPopupData((index: number) => {
              if (this.value[index] == 'A') {
                return this.arrayA
              } else if (this.value[index] == 'B') {
                return this.arrayB
              } else if (this.value[index] == 'C') {
                return this.arrayC
              } else if (this.value[index] == 'L') {
                return this.arrayL
              } else {
                return []
              }
            })
            .onPopupSelect((index: number) => {
              console.info('onPopupSelected:' + index)
            })
        }
        .width('100%')
        .height('100%')
      }
    }
    .backgroundColor(0xDCDCDC)
    .width('100%')
    .height('100%')
  }
}