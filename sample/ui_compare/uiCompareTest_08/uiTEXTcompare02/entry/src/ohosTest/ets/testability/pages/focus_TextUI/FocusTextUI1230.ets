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
@Entry
@Component
struct FocusTextUI1230 {
  @State maxFont: number = 20; // 初始最大字号
  @State maxLine: number = 2; // 初始最大行数

  build() {
    Column() {
      Text('动态参数测试文本：这是一段用于测试的长文本，用于验证maxFontSize和maxLines的效果')
        .fontSize(25)
        .maxFontSize(this.maxFont)
        .maxLines(this.maxLine >= 0 ? this.maxLine : undefined)// 负数时不限制行数
        .width('90%')
        .id('paramBtn1230')
        .onClick(() => {
          this.maxFont = 0;
          this.maxLine = -100;
        })
    }
    .padding(20)
  }
}