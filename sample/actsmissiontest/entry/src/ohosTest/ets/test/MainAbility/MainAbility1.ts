/*
 * Copyright (c) 2022 Huawei Device Co., Ltd.
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
import UIAbility from '@ohos.app.ability.UIAbility';
import base from '@ohos.base';
import { hilog } from '@kit.PerformanceAnalysisKit';
import window from '@ohos.window';
const TAG: string = 'testTag-MainAbility1 ';

export default class MainAbility1 extends UIAbility {
    onCreate(want, launchParam) {
        console.log("[Demo] MainAbility1 onCreate")
    }

    onDestroy() {
        console.log("[Demo] MainAbility1 onDestroy")
    }

    onWindowStageCreate(windowStage) {
        // Main window is created, set main page for this ability
        console.log("[Demo] MainAbility1 onWindowStageCreate")
        windowStage.loadContent('MainAbility/MainAbility1_pages', (err, data) => {
            if (err.code) {
                hilog.error(0x0000, TAG, 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
                return;
            }
            hilog.info(0x0000, TAG, 'Succeeded in loading the content. Data: %{public}s',
                JSON.stringify(data) ?? '');
        });
    }

    onWindowStageDestroy() {
        // Main window is destroyed, release UI related resources
        console.log("[Demo] MainAbility1 onWindowStageDestroy")
    }

    onForeground() {
        console.log("[Demo] MainAbility1 onForeground")

    }

    onBackground() {
        // Ability has back to background
        console.log("[Demo] MainAbility1 onBackground")
    }

    onWindowStageWillDestroy(){
        console.log("[Demo] MainAbility1 onWindowStageWillDestroy")
    }
};
