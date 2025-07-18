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
import hilog from '@ohos.hilog';
import common from '@ohos.app.ability.common';
import Want from '@ohos.app.ability.Want';

let testAbilityWant:Want;
@Entry
@Component
struct Index {
  @State message: string = 'Hello World 222'
  private context:common.UIAbilityContext = getContext(this) as common.UIAbilityContext;
  aboutToAppear() {
    hilog.info(0x0000, 'testTag', '%{public}s', 'TestAbility index aboutToAppear');
    testAbilityWant = AppStorage.get<Want>('TestAbilityWant') as Want;
    hilog.info(0x0000, 'testTag', '%{public}s', 'TestAbility index aboutToAppear ' + JSON.stringify(testAbilityWant));
  }
  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
        EmbeddedComponent({
          bundleName: "com.test.actsabilityerrcodequerysecondtest",
          abilityName: "EntryEmbeddedUIExtAbility",
          parameters:{
            "case":testAbilityWant?.parameters?.case as string
          }
        }, EmbeddedType.EMBEDDED_UI_EXTENSION)

          .width('100%')
          .height('90%')
          .onTerminated((info) => {
            console.log("EntryEmbeddedUIExtAbility Index2: onTerminated, info:" + JSON.stringify(info))
            this.message = 'Termination: code = ' + info.code + ', want = ' + JSON.stringify(info.want);
            this.context.terminateSelf()
          })
          .onError((error) => {
            console.log("EntryEmbeddedUIExtAbility Index2: onError, error:" + JSON.stringify(error))
            this.message = 'Error: code = ' + error.code;
          })
      }.width('100%')
    }.height('100%')
  }
}