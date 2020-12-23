/*
 * Copyright (c) 2020 Huawei Device Co., Ltd.
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

#include <stdio.h>
#include <stdlib.h>
#include "parameter.h"

int main(int argc, char **argv)
{
    printf("******To Obtain Product Params Start******\n");
    char* versionId = GetVersionId();
    if (versionId != nullptr) {
        printf("The VersionID is [%s]\n", versionId);
        free(versionId);
    }

    char* sdkLevel = GetFirstApiLevel();
    if (sdkLevel != nullptr) {
        printf("The Sdk Api Level is [%s]\n", sdkLevel);
        free(sdkLevel);
    }

    char* securityPatchTag = GetSecurityPatchTag();
    if (securityPatchTag != nullptr) {
        printf("The Security Patch is [%s]\n", securityPatchTag);
        free(securityPatchTag);
    }

    char* abiList = GetAbiList();
    if (abiList != nullptr) {
        printf("The AbiList is [%s]\n", abiList);
        free(abiList);
    }

    char* displayVersion = GetDisplayVersion();
    if (displayVersion != nullptr) {
        printf("The OS Version is [%s]\n", displayVersion);
        free(displayVersion);
    }

    char* buildRootHash = GetBuildRootHash();
    if (buildRootHash != nullptr) {
        printf("The BuildRootHash is [%s]\n", buildRootHash);
        free(buildRootHash);
    }

    char* hardWareModel = GetHardwareModel();
    if (hardWareModel != nullptr) {
        printf("The HardwareModel is [%s]\n", hardWareModel);
        free(hardWareModel);
    }

    char* hardWareProfile = GetHardwareProfile();
    if (hardWareProfile != nullptr) {
        printf("The HardwareProfile is [%s]\n", hardWareProfile);
        free(hardWareProfile);
    }

    printf("******To Obtain Product Params End  ******\n");
    return 0;
}