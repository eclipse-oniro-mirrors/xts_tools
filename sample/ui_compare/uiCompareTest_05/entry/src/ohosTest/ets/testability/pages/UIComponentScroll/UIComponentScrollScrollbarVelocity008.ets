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
import { LengthMetrics, LengthUnit } from '@ohos.arkui.node';

@Entry
@Component
struct UIComponentScrollScrollbarVelocity008 {
  scroller: Scroller = new Scroller()
  build() {
    Column({ space: 5 }) {
      Button('test')
        .onClick(()=>{
          this.scroller.fling(1000)
        })
        .id('ScrollbarVelocity008')
        .borderWidth(1)
        WaterFlow({scroller: this.scroller}){
          FlowItem(){
            Text('1')
              .width(50.3).borderWidth(1).height(40.4)
          }
          FlowItem(){
            Text('2')
              .width(50.2).borderWidth(1).height(40.5)
          }
          FlowItem(){
            Text('3')
              .width(50.4).borderWidth(1).height(40.4)
          }
          FlowItem(){
            Text('4')
              .width(50.8).borderWidth(1).height(40.5)
          }
          FlowItem(){
            Text('5')
              .width(50.8).borderWidth(1).height(40.4)
          }
          FlowItem(){
            Text('6')
              .width(50.2).borderWidth(1).height(40.5)
          }
          FlowItem(){
            Text('7')
              .width(50.2).borderWidth(1).height(40.4)
          }
          FlowItem(){
            Text('8')
              .width(50.2).borderWidth(1).height(40.5)
          }
          FlowItem(){
            Text('9')
              .width(50.2).borderWidth(1).height(40.4)
          }
          FlowItem(){
            Text('10')
              .width(50.2).borderWidth(1).height(40.4)
          }
        }
        .id('InterruptAnimation')
        .onAppear(()=>{
          this.scroller.scrollEdge(Edge.Bottom)
        })
        .layoutDirection(FlexDirection.RowReverse)
        .width(100.5)
        .height(100.4)
    }.width('100%')
  }
}
