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

import {Driver , ON} from '@ohos.UiTest'
import uiAppearance from '@ohos.uiAppearance'
import { BusinessError } from '@ohos.base';

export default class Utils {

  static  async  sleep(time : number) :Promise<void> {
    const result:string = await new Promise((resolve:Function)=>{
      setTimeout(()=> {
        resolve('sleep ok')
      },time)
    });
    console.info(result);
  }
  static  async waitAsync (ms:number):Promise<void>{
     return new Promise<void>((resolve)=>{
       setTimeout(resolve,ms)
     })

  }

  static  async clickComponentByKey (componentKey :string){
     let driver = Driver.create();
     let component = await driver.findComponent(ON.id(componentKey))
     await component.click();

  }

  static async setDarkMode(mode:number){
    try {
      uiAppearance.setDarkMode(mode, (error) => {
        if (error) {
          console.error('Set dark-mode failed, ' + error.message);
        } else {
          console.info('Set dark-mode successfully.');
        }
      })
    } catch (error) {
      let message = (error as BusinessError).message;
      console.error('Set dark-mode failed, ' + message);
    }

  }


}




