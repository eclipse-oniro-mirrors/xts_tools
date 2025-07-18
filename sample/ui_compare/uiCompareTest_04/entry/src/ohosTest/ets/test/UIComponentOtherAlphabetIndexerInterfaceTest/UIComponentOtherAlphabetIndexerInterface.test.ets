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
import { describe, beforeAll, beforeEach, afterEach, afterAll, it, expect, Level } from '@ohos/hypium'
import Settings from '../model/Settings'
import windowSnap from '../model/snapShot'
import Logger from '../model/Logger'
import Utils from '../model/Utils'
import { Driver, MouseButton, UiDirection, Component, ON } from '@ohos.UiTest'

export default function UIComponentOtherAlphabetIndexerInterface() {
  describe('UIComponentOtherAlphabetIndexerInterface', () => {
    afterEach(async (done: Function) => {
      if (Settings.windowClass == undefined) {
        return
      }

      Settings.windowClass.destroyWindow((err) => {
        if (err.code) {
          Logger.error('TEST', `Failed to destroy the window. Cause : ${JSON.stringify(err)}`)
          return;
        }
        Logger.info('TEST', `Succeeded in destroy the window.`);
      })
      await Utils.sleep(1000);
      done()
    })

    /*
     * @tc.number  SUB_ACE_UI_COMPONENT_OTHER_ALPHABETINDEXER_INTERFACE_0080
     * @tc.name    Event onPopupSelect (callback: (index: number)=>void)
     * @tc.desc    Component 3 groups
     * @tc.level   0
     */
    it('SUB_ACE_UI_COMPONENT_OTHER_ALPHABETINDEXER_INTERFACE_0080', Level.LEVEL0, async (done: Function) => {
      Logger.info('TEST', `SUB_ACE_UI_COMPONENT_OTHER_ALPHABETINDEXER_INTERFACE_0080 start.`);
      Settings.createWindow("testability/pages/UIComponentOtherAlphabetIndexerInterface/UIComponentOtherAlphabetIndexerInterface001");
      let driver: Driver = Driver.create();
      let alphabetIndexer: Component = await driver.waitForComponent(ON.type('AlphabetIndexer'), 1000);
      let point = await alphabetIndexer.getBoundsCenter();
      await driver.mouseClick({x:point.x, y: point.y - 150}, MouseButton.MOUSE_BUTTON_LEFT);
      await driver.waitForIdle(500, 1000);
      await driver.mouseLongClick({x:point.x + 120, y: point.y }, MouseButton.MOUSE_BUTTON_LEFT);
      await driver.waitForIdle(500, 1000);
      windowSnap.snapShot();
      await Utils.sleep(1000);
      Logger.info('TEST', `SUB_ACE_UI_COMPONENT_OTHER_ALPHABETINDEXER_INTERFACE_0080 finish.`);
      done();
    });

    /*
     * @tc.number  SUB_ACE_UI_COMPONENT_OTHER_ALPHABETINDEXER_INTERFACE_0090
     * @tc.name    Event onRequestPopupData (callback: (index: number)=>Array)
     * @tc.desc    Component 3 groups
     * @tc.level   0
     */
    it('SUB_ACE_UI_COMPONENT_OTHER_ALPHABETINDEXER_INTERFACE_0090', Level.LEVEL0, async (done: Function) => {
      Logger.info('TEST', `SUB_ACE_UI_COMPONENT_OTHER_ALPHABETINDEXER_INTERFACE_0090 start.`);
      Settings.createWindow("testability/pages/UIComponentOtherAlphabetIndexerInterface/UIComponentOtherAlphabetIndexerInterface002");
      let driver: Driver = Driver.create();
      let alphabetIndexer: Component = await driver.waitForComponent(ON.type('AlphabetIndexer'), 1000);
      let point = await alphabetIndexer.getBoundsCenter();
      await driver.mouseClick({x: point.x, y: point.y - 150}, MouseButton.MOUSE_BUTTON_LEFT);
      await driver.waitForIdle(500, 1000);
      await driver.fling(UiDirection.DOWN, 10000);
      await driver.mouseScroll({x: point.x + 120, y: point.y }, true, 70, MouseButton.MOUSE_BUTTON_LEFT);
      await driver.waitForIdle(500, 2000);
      windowSnap.snapShot();
      await Utils.sleep(1000);
      Logger.info('TEST', `SUB_ACE_UI_COMPONENT_OTHER_ALPHABETINDEXER_INTERFACE_0090 finish.`);
      done();
    });
  })
}
