/*
 * Copyright (c) 2022-2023 Huawei Device Co., Ltd.
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

import AbilityDelegatorRegistry from '@ohos.app.ability.abilityDelegatorRegistry';
import UIAbility from '@ohos.app.ability.UIAbility';
import { Hypium } from '@ohos/hypium';
import testsuite from '../test/List.test';
import Logger from '../utils/Logger';

export default class TestAbility extends UIAbility {
  onCreate(want, launchParam): void {
    Logger.info('TestAbility onCreate');
    let abilityDelegator = AbilityDelegatorRegistry.getAbilityDelegator();
    let abilityDelegatorArguments = AbilityDelegatorRegistry.getArguments();
    Logger.info('start run testcase!!!');
    Hypium.hypiumTest(abilityDelegator, abilityDelegatorArguments, testsuite);
  }

  onDestroy(): void {
    Logger.info('TestAbility onDestroy');
  }

  onWindowStageCreate(windowStage): void {
    Logger.info('TestAbility onWindowStageCreate');
    windowStage.loadContent('testability/pages/Index', (err, data) => {
      if (err.code) {
        console.error('Failed to load the content. Cause:' + JSON.stringify(err));
        return;
      }
      Logger.info('Succeeded in loading the content. Data: ' + JSON.stringify(data));
    });

    globalThis.abilityContext = this.context;
  }

  onWindowStageDestroy(): void {
    Logger.info('TestAbility onWindowStageDestroy');
  }

  onForeground(): void {
    Logger.info('TestAbility onForeground');
  }

  onBackground(): void {
    Logger.info('TestAbility onBackground');
  }
}