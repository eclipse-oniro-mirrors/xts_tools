/*
 * Copyright (c) 2024 Shenzhen Kaihong Digital Industry Development Co., Ltd.
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
struct UIComponentLayoutStack015 {
  @State name: string = 'UIComponentLayoutStack015';
  @State alignContent: Alignment = Alignment.TopStart;
  myXComponentController: XComponentController = new XComponentController();
  @State stackWidth: number = 0;
  @State stackHeight: number = 0;

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Start }) {

      Button('获取Stack组价尺寸')
        .id(this.name + '_001')
        .onClick(() => {
          let context = this.getUIContext();
          let info = context.getComponentUtils().getRectangleById(this.name + '_003');
          this.stackWidth = info.size.width;
          this.stackWidth = context.px2vp(this.stackWidth);
          this.stackHeight = info.size.height;
          this.stackHeight = context.px2vp(this.stackHeight);
        })
      Text('组件宽度: ' + this.stackWidth.toString())
      Text('组件高度: ' + this.stackHeight.toString())

      XComponent({
        id: this.name + '_002',
        type: XComponentType.NODE,
        libraryname: 'nativerender',
        controller: this.myXComponentController
      }) {
        Stack({ }) {
          Text('This is a Text component1').width('80%').height('60%').backgroundColor(0xd2cab3)
          Text('This is a Text component2').width('60%').height('40%').backgroundColor(0xd2cab3)
        }
        .width(200.5)
        .height(200.5)
        .id(this.name + '_003')
      }
      .width('100%')
      .height('100%')

    }
    .width('100%')
    .height('100%')
  }
}