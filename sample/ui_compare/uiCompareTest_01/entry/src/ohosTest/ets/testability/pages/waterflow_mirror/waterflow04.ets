/**
 * Copyright (c) 2025 Shenzhen Kaihong Digital Industry Development Co., Ltd.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import { WaterFlowDataSource } from './WaterFlowDataSource';

@Entry
@Component
struct WaterFlow04 {
  @State minSize: number = 80;
  @State maxSize: number = 180;
  @State fontSize: number = 24;
  @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
  @State layoutDirectionArray:Array<FlexDirection> = [
    FlexDirection.Row,
    FlexDirection.RowReverse,
    FlexDirection.Column,
    FlexDirection.ColumnReverse
  ]
  @State layoutDirection:FlexDirection = FlexDirection.Row
  @State arrayIndex:number = 0
  @State rowWidth:Length = '30%'
  scroller: Scroller = new Scroller();
  dataSource: WaterFlowDataSource = new WaterFlowDataSource();
  private itemWidthArray: number[] = [];
  private itemHeightArray: number[] = [];

  // 计算FlowItem宽/高
  getSize() {
    let ret = Math.floor(Math.random() * this.maxSize);
    return (ret > this.minSize ? ret : this.minSize);
  }

  // 设置FlowItem的宽/高数组
  setItemSizeArray() {
    for (let i = 0; i < 100; i++) {
      this.itemWidthArray.push(this.getSize());
      this.itemHeightArray.push(this.getSize());
    }
  }

  aboutToAppear() {
    this.setItemSizeArray();
  }

  @Builder
  itemFoot() {
    Column() {
      Text(`Footer`)
        .fontSize(10)
        .backgroundColor(Color.Red)
        .width(50)
        .height(50)
        .align(Alignment.Center)
        .margin({ top: 2 })
    }
  }

  build() {
    Column({ space: 2 }) {
      WaterFlow({scroller:this.scroller}) {
        LazyForEach(this.dataSource, (item: number) => {
          FlowItem() {
            Column() {
              Text("N" + item).fontSize(12).height('16')
              // 存在对应的jpg文件才会显示图片
              Image($r('app.media.icon'))
                .objectFit(ImageFit.Fill)
                .width('100%')
                .layoutWeight(1)
              Button('waterFlow' + item)
            }
          }
          .onAppear(() => {
            // 即将触底时提前增加数据
            if (item + 20 == this.dataSource.totalCount()) {
              for (let i = 0; i < 100; i++) {
                this.dataSource.addLastItem();
              }
            }
          })
          .width(this.rowWidth)
          .height(this.itemHeightArray[item % 100])
          .backgroundColor(this.colors[item % 5])
        }, (item: string) => item)
      }
      .id('WaterFlow04')
      .direction(Direction.Rtl)
      .layoutDirection(this.layoutDirection)
      .columnsGap(10)
      .rowsGap(5)
      .backgroundColor(0xFAEEE0)
      .width('100%')
      .height('90%')
      .onReachStart(() => {
        console.info('waterFlow reach start');
      })
      .onScrollStart(() => {
        console.info('waterFlow scroll start');
      })
      .onScrollStop(() => {
        console.info('waterFlow scroll stop');
      })
      .onScrollFrameBegin((offset: number, state: ScrollState) => {
        console.info('waterFlow scrollFrameBegin offset: ' + offset + ' state: ' + state.toString());
        return { offsetRemain: offset };
      })

      Button('changeLayoutDirection')
        .id('changeLayoutDirection04')
        .height('5%')
        .onClick(() => { // 点击后下滑指定距离600vp
          this.layoutDirection = this.layoutDirectionArray[this.arrayIndex]
          if(this.arrayIndex == 0 || this.arrayIndex == 1){
            this.rowWidth = '30%'
          }else {
            this.rowWidth = '100%'
          }
          this.arrayIndex++
          if(this.arrayIndex == 4){
            this.arrayIndex = 0
          }
        })
        .margin({ top: 10, left: 20 })
    }
  }
}
