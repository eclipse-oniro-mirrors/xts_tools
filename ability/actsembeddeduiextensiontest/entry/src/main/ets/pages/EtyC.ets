/*
 * Copyright (C) 2024 Huawei Device Co., Ltd.
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
import { Want } from '@kit.AbilityKit';
import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct EtyB {
  @State message: string = 'Hello World';
  private want: Want = {
    bundleName: 'com.example.assistappa',
    abilityName: 'EmbeddedUIExtAbilityInstance',
    parameters: {

    }
  }

  build() {
    Row() {
      Column() {
        Text(this.message).fontSize(30)
        EmbeddedComponent(this.want, EmbeddedType.EMBEDDED_UI_EXTENSION)
          .width('100%')
          .height('90%')
          .onTerminated((info: TerminationInfo) => {
            this.message = 'Terminarion: code = ' + info.code + ', want = ' + JSON.stringify(info.want);
            console.log('shuzi',JSON.stringify(EmbeddedType.EMBEDDED_UI_EXTENSION))
          })
          .onError((error: BusinessError) => {
            this.message = 'Error: code = ' + error.code;
            console.log('instance',JSON.stringify(error))
            let commonEventPublishData: commonEventManager.CommonEventPublishData ={
              parameters:{
                data: error.code
              }
            }
            commonEventManager.publish('ExtensionInstance', commonEventPublishData, async (error) =>{
              hilog.info(0x0000, 'testTag1', '%{public}s', `Embeddedextension publish: ${JSON.stringify(error)}`);
            })
          })
        EmbeddedComponent(this.want, EmbeddedType.EMBEDDED_UI_EXTENSION)
          .width('100%')
          .height('90%')
          .onTerminated((info: TerminationInfo) => {
            this.message = 'Terminarion: code = ' + info.code + ', want = ' + JSON.stringify(info.want);
            console.log('shuzi',JSON.stringify(EmbeddedType.EMBEDDED_UI_EXTENSION))
          })
          .onError((error: BusinessError) => {
            this.message = 'Error: code = ' + error.code;
            console.log('instance',JSON.stringify(error))
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}