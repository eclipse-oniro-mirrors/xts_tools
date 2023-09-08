"""
 * Copyright (c) 2023 iSoftStone Information Technology (Group) Co.,Ltd.
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
"""

import unittest
from Tool import WebView

class Test(unittest.TestCase):
    @classmethod  # ��ʼ�����Ի�����ֻ��ִ��һ��
    def setUp(self) -> None:
        self.LE = WebView()
        self.LE.init_webview(test_package='com.example.myapplication')  # ����chromeDriver

    def test_css_001(self):
        self.LE.init_runner('test_css_001')  # ��runnerҳ��
        #self.LE.click_js()  # ȡ����ѡjs
        #self.LE.click_manual()  # ȡ����ѡmanual
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/abspos-containing-block-initial-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        #self.LE.start_test()  # ���start test ��ť
        #self.LE.click_show_test()  # ���show test��ť
        self.LE.start_show_test("css_1")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_001')

    def test_css_002(self):
        self.LE.init_runner('test_css_002')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/abspos-containing-block-initial-004a.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_2")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_002')

    def test_css_003(self):
        self.LE.init_runner('test_css_003')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/abspos-containing-block-initial-004b.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_3")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_003')

    def test_css_004(self):
        self.LE.init_runner('test_css_004')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/abspos-containing-block-initial-004c.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_4")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_004')

    def test_css_005(self):
        self.LE.init_runner('test_css_005')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/abspos-containing-block-initial-004d.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_5")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_005')

    def test_css_006(self):
        self.LE.init_runner('test_css_006')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/abspos-containing-block-initial-004e.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_6")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_006')

    def test_css_007(self):
        self.LE.init_runner('test_css_007')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/abspos-containing-block-initial-004f.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_7")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_007')

    def test_css_008(self):
        self.LE.init_runner('test_css_008')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/abspos-containing-block-initial-005a.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_8")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_008')

    def test_css_009(self):
        self.LE.init_runner('test_css_009')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/abspos-containing-block-initial-005b.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_9")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_009')

    def test_css_010(self):
        self.LE.init_runner('test_css_010')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/abspos-containing-block-initial-005c.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_10")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_010')

    def test_css_011(self):
        self.LE.init_runner('test_css_011')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/abspos-containing-block-initial-005d.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_11")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_011')

    def test_css_012(self):
        self.LE.init_runner('test_css_012')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/abspos-containing-block-initial-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_12")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_012')

    def test_css_013(self):
        self.LE.init_runner('test_css_013')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/abspos-containing-block-initial-009a.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_13")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_013')

    def test_css_014(self):
        self.LE.init_runner('test_css_014')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/abspos-containing-block-initial-009b.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_14")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_014')

    def test_css_015(self):
        self.LE.init_runner('test_css_015')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/abspos-containing-block-initial-009e.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_15")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_015')

    def test_css_016(self):
        self.LE.init_runner('test_css_016')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/abspos-containing-block-initial-009f.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_16")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_016')

    def test_css_017(self):
        self.LE.init_runner('test_css_017')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/between-float-and-text.html')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_17")
        self.LE.test_screenshot('/html/body/div/div[1]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('/html/body/div/div[2]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_screenshot('/html/body/div', "ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_017')

    def test_css_018(self):
        self.LE.init_runner('test_css_018')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/hypothetical-box-dynamic.html')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_18")
        self.LE.test_screenshot('/html/body/div[1]/span', "test")  # testҳ���ͼ
        self.LE.test_screenshot('/html/body/div[2]/span', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_screenshot('/html/body/div[1]/span', "ref")  # referenceҳ���ͼ
        self.LE.ref_screenshot('/html/body/div[2]/span', "ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_018')

    def test_css_019(self):
        self.LE.init_runner('test_css_019')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/hypothetical-inline-alone-on-second-line.html')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_19")
        self.LE.test_screenshot('/html/body/span/span', "test")  # testҳ���ͼ
        self.LE.test_screenshot('/html/body/span', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_screenshot('/html/body/div', "ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_019')

    def test_css_020(self):
        self.LE.init_runner('test_css_020')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/remove-block-between-inline-and-abspos.html')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_20")
        self.LE.test_implicit_expression_screenshot('/html/body/div', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_implicit_expression_screenshot('/html/body/div', "ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_020')

    def test_css_021(self):
        self.LE.init_runner('test_css_021')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/static-inside-table-cell.html')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_21")
        self.LE.test_screenshot('//*[@id="container"]/div[2]/div[1]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_021')

    def test_css_022(self):
        self.LE.init_runner('test_css_022')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/table-caption-is-containing-block-001.html')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_22")
        self.LE.test_screenshot('//*[@id="redSquare"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_022')

    def test_css_023(self):
        self.LE.init_runner('test_css_023')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/abspos/table-caption-passes-abspos-up-001.html')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_23")
        self.LE.test_screenshot('//*[@id="redSquare"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_023')

    def test_css_024(self):
        self.LE.init_runner('test_css_024')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_24")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_024')

    def test_css_025(self):
        self.LE.init_runner('test_css_025')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_25")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_025')

    def test_css_026(self):
        self.LE.init_runner('test_css_026')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_26")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_026')

    def test_css_027(self):
        self.LE.init_runner('test_css_027')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_27")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_027')

    def test_css_028(self):
        self.LE.init_runner('test_css_028')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_28")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_028')

    def test_css_029(self):
        self.LE.init_runner('test_css_029')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_29")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_029')

    def test_css_030(self):
        self.LE.init_runner('test_css_030')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_30")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_030')

    def test_css_031(self):
        self.LE.init_runner('test_css_031')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-008.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_31")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_031')

    def test_css_032(self):
        self.LE.init_runner('test_css_032')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_32")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_032')

    def test_css_033(self):
        self.LE.init_runner('test_css_033')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-010.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_33")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_033')

    def test_css_034(self):
        self.LE.init_runner('test_css_034')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-014.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_34")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_034')

    def test_css_035(self):
        self.LE.init_runner('test_css_035')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-016.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_35")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_035')

    def test_css_036(self):
        self.LE.init_runner('test_css_036')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-017.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_36")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_036')

    def test_css_037(self):
        self.LE.init_runner('test_css_037')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-018.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_37")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_037')

    def test_css_038(self):
        self.LE.init_runner('test_css_038')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-020.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_38")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_038')

    def test_css_039(self):
        self.LE.init_runner('test_css_039')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-021.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_39")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_039')

    def test_css_040(self):
        self.LE.init_runner('test_css_040')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-022.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_40")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_040')

    def test_css_041(self):
        self.LE.init_runner('test_css_041')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-024.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_41")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_041')

    def test_css_042(self):
        self.LE.init_runner('test_css_042')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-025.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_42")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_042')

    def test_css_043(self):
        self.LE.init_runner('test_css_043')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-026.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_43")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_043')

    def test_css_044(self):
        self.LE.init_runner('test_css_044')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-029.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_44")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_044')

    def test_css_045(self):
        self.LE.init_runner('test_css_045')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-030.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_45")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_045')

    def test_css_046(self):
        self.LE.init_runner('test_css_046')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-031.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_46")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_046')

    def test_css_047(self):
        self.LE.init_runner('test_css_047')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-033.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_47")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_047')

    def test_css_048(self):
        self.LE.init_runner('test_css_048')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-034.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_48")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_048')

    def test_css_049(self):
        self.LE.init_runner('test_css_049')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-036.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_49")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_049')

    def test_css_050(self):
        self.LE.init_runner('test_css_050')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-037.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_50")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_050')

    def test_css_051(self):
        self.LE.init_runner('test_css_051')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-038.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_51")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_051')

    def test_css_052(self):
        self.LE.init_runner('test_css_052')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-041.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_52")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_052')

    def test_css_053(self):
        self.LE.init_runner('test_css_053')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-043.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_53")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_053')

    def test_css_054(self):
        self.LE.init_runner('test_css_054')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-048.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_54")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_054')

    def test_css_055(self):
        self.LE.init_runner('test_css_055')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-050.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_55")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_055')

    def test_css_056(self):
        self.LE.init_runner('test_css_056')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-051.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_56")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_056')

    def test_css_057(self):
        self.LE.init_runner('test_css_057')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-052.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_57")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_057')

    def test_css_058(self):
        self.LE.init_runner('test_css_058')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-053.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_58")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_058')

    def test_css_059(self):
        self.LE.init_runner('test_css_059')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-055.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_59")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_059')

    def test_css_060(self):
        self.LE.init_runner('test_css_060')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-056.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_60")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_060')

    def test_css_061(self):
        self.LE.init_runner('test_css_061')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-058.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_61")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_061')

    def test_css_062(self):
        self.LE.init_runner('test_css_062')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-059.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_62")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_062')

    def test_css_063(self):
        self.LE.init_runner('test_css_063')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-060.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_63")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_063')

    def test_css_064(self):
        self.LE.init_runner('test_css_064')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-061.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_64")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_064')

    def test_css_065(self):
        self.LE.init_runner('test_css_065')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-063.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_65")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_065')

    def test_css_066(self):
        self.LE.init_runner('test_css_066')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-064.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_66")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_066')

    def test_css_067(self):
        self.LE.init_runner('test_css_067')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-068.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_67")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_067')

    def test_css_068(self):
        self.LE.init_runner('test_css_068')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-070.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_68")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_068')

    def test_css_069(self):
        self.LE.init_runner('test_css_069')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-071.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_69")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_069')

    def test_css_070(self):
        self.LE.init_runner('test_css_070')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-073.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_70")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_070')

    def test_css_071(self):
        self.LE.init_runner('test_css_071')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-075.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_71")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_071')

    def test_css_072(self):
        self.LE.init_runner('test_css_072')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-076.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_72")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_072')

    def test_css_073(self):
        self.LE.init_runner('test_css_073')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-078.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_73")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_073')

    def test_css_074(self):
        self.LE.init_runner('test_css_074')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-080.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_74")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_074')

    def test_css_075(self):
        self.LE.init_runner('test_css_075')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-081.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_75")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_075')

    def test_css_076(self):
        self.LE.init_runner('test_css_076')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-082.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_76")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_076')

    def test_css_077(self):
        self.LE.init_runner('test_css_077')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-083.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_77")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_077')

    def test_css_078(self):
        self.LE.init_runner('test_css_078')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-085.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_78")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_078')

    def test_css_079(self):
        self.LE.init_runner('test_css_079')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-087.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_79")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_079')

    def test_css_080(self):
        self.LE.init_runner('test_css_080')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-090.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_80")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_080')

    def test_css_081(self):
        self.LE.init_runner('test_css_081')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-093.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_81")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_081')

    def test_css_082(self):
        self.LE.init_runner('test_css_082')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-095.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_82")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_082')

    def test_css_083(self):
        self.LE.init_runner('test_css_083')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-096.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_83")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_083')

    def test_css_084(self):
        self.LE.init_runner('test_css_084')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-097.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_84")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_084')

    def test_css_085(self):
        self.LE.init_runner('test_css_085')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-101.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_85")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_085')

    def test_css_086(self):
        self.LE.init_runner('test_css_086')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-103.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_86")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_086')

    def test_css_087(self):
        self.LE.init_runner('test_css_087')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-104.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_87")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_087')

    def test_css_088(self):
        self.LE.init_runner('test_css_088')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-106.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_88")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_088')

    def test_css_089(self):
        self.LE.init_runner('test_css_089')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-107.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_89")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_089')

    def test_css_090(self):
        self.LE.init_runner('test_css_090')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-109.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_90")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_090')

    def test_css_091(self):
        self.LE.init_runner('test_css_091')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-111.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_91")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_091')

    def test_css_092(self):
        self.LE.init_runner('test_css_092')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-114.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_92")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_092')

    def test_css_093(self):
        self.LE.init_runner('test_css_093')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-117.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_93")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_093')

    def test_css_094(self):
        self.LE.init_runner('test_css_094')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-120.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_94")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_094')

    def test_css_095(self):
        self.LE.init_runner('test_css_095')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-128.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_95")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_095')

    def test_css_096(self):
        self.LE.init_runner('test_css_096')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-130.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_96")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_096')

    def test_css_097(self):
        self.LE.init_runner('test_css_097')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-135.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_97")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_097')

    def test_css_098(self):
        self.LE.init_runner('test_css_098')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-137.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_98")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_098')

    def test_css_099(self):
        self.LE.init_runner('test_css_099')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-138.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_99")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_099')

    def test_css_100(self):
        self.LE.init_runner('test_css_100')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-139.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_100")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_100')

    def test_css_101(self):
        self.LE.init_runner('test_css_101')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-141.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_101")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_101')

    def test_css_102(self):
        self.LE.init_runner('test_css_102')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-144.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_102")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_102')

    def test_css_103(self):
        self.LE.init_runner('test_css_103')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-147.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_103")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_103')

    def test_css_104(self):
        self.LE.init_runner('test_css_104')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-150.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_104")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_104')

    def test_css_105(self):
        self.LE.init_runner('test_css_105')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-152.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_105")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_105')

    def test_css_106(self):
        self.LE.init_runner('test_css_106')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-153.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_106")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_106')

    def test_css_107(self):
        self.LE.init_runner('test_css_107')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-154.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_107")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_107')

    def test_css_108(self):
        self.LE.init_runner('test_css_108')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-156.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_108")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_108')

    def test_css_109(self):
        self.LE.init_runner('test_css_109')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-161.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_109")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_109')

    def test_css_110(self):
        self.LE.init_runner('test_css_110')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-163.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_110")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_110')

    def test_css_111(self):
        self.LE.init_runner('test_css_111')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-171.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_111")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_111')

    def test_css_112(self):
        self.LE.init_runner('test_css_112')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-174.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_112")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_112')

    def test_css_113(self):
        self.LE.init_runner('test_css_113')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-177.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_113")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_113')

    def test_css_114(self):
        self.LE.init_runner('test_css_114')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-180.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_114")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_114')

    def test_css_115(self):
        self.LE.init_runner('test_css_115')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-182.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_115")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_115')

    def test_css_116(self):
        self.LE.init_runner('test_css_116')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-184.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_116")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_116')

    def test_css_117(self):
        self.LE.init_runner('test_css_117')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-185.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_117")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_117')

    def test_css_118(self):
        self.LE.init_runner('test_css_118')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-187.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_118")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_118')

    def test_css_119(self):
        self.LE.init_runner('test_css_119')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-188.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_119")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_119')

    def test_css_120(self):
        self.LE.init_runner('test_css_120')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-190.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_120")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_120')

    def test_css_121(self):
        self.LE.init_runner('test_css_121')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-194.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_121")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_121')

    def test_css_122(self):
        self.LE.init_runner('test_css_122')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-195.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_122")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_122')

    def test_css_123(self):
        self.LE.init_runner('test_css_123')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-196.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_123")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_123')

    def test_css_124(self):
        self.LE.init_runner('test_css_124')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-198.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_124")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_124')

    def test_css_125(self):
        self.LE.init_runner('test_css_125')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-201.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_125")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_125')

    def test_css_126(self):
        self.LE.init_runner('test_css_126')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-204.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_126")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_126')

    def test_css_127(self):
        self.LE.init_runner('test_css_127')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-326.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_127")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_127')

    def test_css_128(self):
        self.LE.init_runner('test_css_128')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-327.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_128")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_128')

    def test_css_129(self):
        self.LE.init_runner('test_css_129')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-328.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_129")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_129')

    def test_css_130(self):
        self.LE.init_runner('test_css_130')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-329.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_130")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_130')

    def test_css_131(self):
        self.LE.init_runner('test_css_131')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-applies-to-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_131")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_131')

    def test_css_132(self):
        self.LE.init_runner('test_css_132')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-applies-to-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_132")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_132')

    def test_css_133(self):
        self.LE.init_runner('test_css_133')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-applies-to-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_133")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_133')

    def test_css_134(self):
        self.LE.init_runner('test_css_134')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-applies-to-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_134")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_134')

    def test_css_135(self):
        self.LE.init_runner('test_css_135')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-applies-to-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_135")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_135')

    def test_css_136(self):
        self.LE.init_runner('test_css_136')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-applies-to-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_136")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_136')

    def test_css_137(self):
        self.LE.init_runner('test_css_137')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-applies-to-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_137")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_137')

    def test_css_138(self):
        self.LE.init_runner('test_css_138')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-applies-to-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_138")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_138')

    def test_css_139(self):
        self.LE.init_runner('test_css_139')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-applies-to-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_139")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_139')

    def test_css_140(self):
        self.LE.init_runner('test_css_140')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-applies-to-013.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_140")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_140')

    def test_css_141(self):
        self.LE.init_runner('test_css_141')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-applies-to-014.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_141")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_141')

    def test_css_142(self):
        self.LE.init_runner('test_css_142')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-applies-to-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_142")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_142')

    def test_css_143(self):
        self.LE.init_runner('test_css_143')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-attachment-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_143")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_143')

    def test_css_144(self):
        self.LE.init_runner('test_css_144')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-attachment-applies-to-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_144")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_144')

    def test_css_145(self):
        self.LE.init_runner('test_css_145')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-attachment-applies-to-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_145")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_145')

    def test_css_146(self):
        self.LE.init_runner('test_css_146')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-attachment-applies-to-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_146")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_146')

    def test_css_147(self):
        self.LE.init_runner('test_css_147')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-attachment-applies-to-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_147")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_147')

    def test_css_148(self):
        self.LE.init_runner('test_css_148')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-attachment-applies-to-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_148")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_148')

    def test_css_149(self):
        self.LE.init_runner('test_css_149')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-attachment-applies-to-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_149")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_149')

    def test_css_150(self):
        self.LE.init_runner('test_css_150')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-attachment-applies-to-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_150")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_150')

    def test_css_151(self):
        self.LE.init_runner('test_css_151')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-attachment-applies-to-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_151")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_151')

    def test_css_152(self):
        self.LE.init_runner('test_css_152')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-attachment-applies-to-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_152")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_152')

    def test_css_153(self):
        self.LE.init_runner('test_css_153')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-attachment-applies-to-013.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_153")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_153')

    def test_css_154(self):
        self.LE.init_runner('test_css_154')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-attachment-applies-to-014.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_154")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_154')

    def test_css_155(self):
        self.LE.init_runner('test_css_155')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-attachment-applies-to-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_155")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_155')

    def test_css_156(self):
        self.LE.init_runner('test_css_156')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-bg-pos-204.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_156")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_156')

    def test_css_157(self):
        self.LE.init_runner('test_css_157')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-bg-pos-206.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_157")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_157')

    def test_css_158(self):
        self.LE.init_runner('test_css_158')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-bg-pos-208.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_158")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_158')

    def test_css_159(self):
        self.LE.init_runner('test_css_159')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-body-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_159")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_159')

    def test_css_160(self):
        self.LE.init_runner('test_css_160')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_160")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_160')

    def test_css_161(self):
        self.LE.init_runner('test_css_161')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_161")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_161')

    def test_css_162(self):
        self.LE.init_runner('test_css_162')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_162")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_162')

    def test_css_163(self):
        self.LE.init_runner('test_css_163')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_163")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_163')

    def test_css_164(self):
        self.LE.init_runner('test_css_164')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_164")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_164')

    def test_css_165(self):
        self.LE.init_runner('test_css_165')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_165")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_165')

    def test_css_166(self):
        self.LE.init_runner('test_css_166')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_166")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_166')

    def test_css_167(self):
        self.LE.init_runner('test_css_167')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-008.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_167")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_167')

    def test_css_168(self):
        self.LE.init_runner('test_css_168')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_168")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_168')

    def test_css_169(self):
        self.LE.init_runner('test_css_169')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-010.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_169")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_169')

    def test_css_170(self):
        self.LE.init_runner('test_css_170')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-011.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_170")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_170')

    def test_css_171(self):
        self.LE.init_runner('test_css_171')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_test()  # ���start test ��ť
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_171')

    def test_css_172(self):
        self.LE.init_runner('test_css_172')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-013.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_171")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_172')

    def test_css_173(self):
        self.LE.init_runner('test_css_173')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-014.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_172")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_173')

    def test_css_174(self):
        self.LE.init_runner('test_css_174')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_173")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_174')

    def test_css_175(self):
        self.LE.init_runner('test_css_175')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-016.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_174")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_175')

    def test_css_176(self):
        self.LE.init_runner('test_css_176')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-017.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_175")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_176')

    def test_css_177(self):
        self.LE.init_runner('test_css_177')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-018.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_176")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_177')

    def test_css_178(self):
        self.LE.init_runner('test_css_178')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-019.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_177")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_178')

    def test_css_179(self):
        self.LE.init_runner('test_css_179')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-020.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_178")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_179')

    def test_css_180(self):
        self.LE.init_runner('test_css_180')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-021.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_179")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_180')

    def test_css_181(self):
        self.LE.init_runner('test_css_181')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-022.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_180")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_181')

    def test_css_182(self):
        self.LE.init_runner('test_css_182')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-023.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_181")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_182')

    def test_css_183(self):
        self.LE.init_runner('test_css_183')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-024.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_182")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_183')

    def test_css_184(self):
        self.LE.init_runner('test_css_184')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-025.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_183")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_184')

    def test_css_185(self):
        self.LE.init_runner('test_css_185')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-026.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_184")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_185')

    def test_css_186(self):
        self.LE.init_runner('test_css_186')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-027.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_185")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_186')

    def test_css_187(self):
        self.LE.init_runner('test_css_187')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-028.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_186")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_187')

    def test_css_188(self):
        self.LE.init_runner('test_css_188')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-029.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_187")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_188')

    def test_css_189(self):
        self.LE.init_runner('test_css_189')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-030.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_188")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_189')

    def test_css_190(self):
        self.LE.init_runner('test_css_190')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-031.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_189")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_190')

    def test_css_191(self):
        self.LE.init_runner('test_css_191')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-032.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_190")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_191')

    def test_css_192(self):
        self.LE.init_runner('test_css_192')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-033.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_191")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_192')

    def test_css_193(self):
        self.LE.init_runner('test_css_193')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-034.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_192")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_193')

    def test_css_194(self):
        self.LE.init_runner('test_css_194')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-035.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_193")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_194')

    def test_css_195(self):
        self.LE.init_runner('test_css_195')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-036.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_194")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_195')

    def test_css_196(self):
        self.LE.init_runner('test_css_196')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-037.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_195")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_196')

    def test_css_197(self):
        self.LE.init_runner('test_css_197')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-038.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_196")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_197')

    def test_css_198(self):
        self.LE.init_runner('test_css_198')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-039.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_197")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_198')

    def test_css_199(self):
        self.LE.init_runner('test_css_199')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-040.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_198")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_199')

    def test_css_200(self):
        self.LE.init_runner('test_css_200')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-041.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_199")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_200')

    def test_css_201(self):
        self.LE.init_runner('test_css_201')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-042.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_200")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_201')

    def test_css_202(self):
        self.LE.init_runner('test_css_202')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-043.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_201")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_202')

    def test_css_203(self):
        self.LE.init_runner('test_css_203')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-044.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_202")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_203')

    def test_css_204(self):
        self.LE.init_runner('test_css_204')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-045.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_203")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_204')

    def test_css_205(self):
        self.LE.init_runner('test_css_205')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-046.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_204")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_205')

    def test_css_206(self):
        self.LE.init_runner('test_css_206')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-047.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_205")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_206')

    def test_css_207(self):
        self.LE.init_runner('test_css_207')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-048.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_206")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_207')

    def test_css_208(self):
        self.LE.init_runner('test_css_208')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-049.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_207")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_208')

    def test_css_209(self):
        self.LE.init_runner('test_css_209')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-050.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_208")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_209')

    def test_css_210(self):
        self.LE.init_runner('test_css_210')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-051.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_209")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_210')

    def test_css_211(self):
        self.LE.init_runner('test_css_211')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-052.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_210")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_211')

    def test_css_212(self):
        self.LE.init_runner('test_css_212')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-053.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_211")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_212')

    def test_css_213(self):
        self.LE.init_runner('test_css_213')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-054.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_212")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_213')

    def test_css_214(self):
        self.LE.init_runner('test_css_214')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-055.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_213")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_214')

    def test_css_215(self):
        self.LE.init_runner('test_css_215')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-056.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_214")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_215')

    def test_css_216(self):
        self.LE.init_runner('test_css_216')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-057.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_215")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_216')

    def test_css_217(self):
        self.LE.init_runner('test_css_217')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-058.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_216")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_217')

    def test_css_218(self):
        self.LE.init_runner('test_css_218')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-059.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_217")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_218')

    def test_css_219(self):
        self.LE.init_runner('test_css_219')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-060.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_218")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_219')

    def test_css_220(self):
        self.LE.init_runner('test_css_220')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-061.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_219")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_220')

    def test_css_221(self):
        self.LE.init_runner('test_css_221')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-062.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_220")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_221')

    def test_css_222(self):
        self.LE.init_runner('test_css_222')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-063.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_221")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_222')

    def test_css_223(self):
        self.LE.init_runner('test_css_223')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-064.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_222")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_223')

    def test_css_224(self):
        self.LE.init_runner('test_css_224')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-065.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_223")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_224')

    def test_css_225(self):
        self.LE.init_runner('test_css_225')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-066.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_224")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_225')

    def test_css_226(self):
        self.LE.init_runner('test_css_226')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-067.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_225")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_226')

    def test_css_227(self):
        self.LE.init_runner('test_css_227')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-068.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_226")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_227')

    def test_css_228(self):
        self.LE.init_runner('test_css_228')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-069.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_227")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_228')

    def test_css_229(self):
        self.LE.init_runner('test_css_229')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-070.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_228")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_229')

    def test_css_230(self):
        self.LE.init_runner('test_css_230')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-071.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_229")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_230')

    def test_css_231(self):
        self.LE.init_runner('test_css_231')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-072.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_230")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_231')

    def test_css_232(self):
        self.LE.init_runner('test_css_232')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-073.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_231")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_232')

    def test_css_233(self):
        self.LE.init_runner('test_css_233')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-074.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_232")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_233')

    def test_css_234(self):
        self.LE.init_runner('test_css_234')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-075.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_233")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_234')

    def test_css_235(self):
        self.LE.init_runner('test_css_235')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-076.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_234")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_235')

    def test_css_236(self):
        self.LE.init_runner('test_css_236')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-077.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_235")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_236')

    def test_css_237(self):
        self.LE.init_runner('test_css_237')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-078.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_236")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_237')

    def test_css_238(self):
        self.LE.init_runner('test_css_238')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-079.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_237")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_238')

    def test_css_239(self):
        self.LE.init_runner('test_css_239')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-080.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_238")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_239')

    def test_css_240(self):
        self.LE.init_runner('test_css_240')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-081.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_239")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_240')

    def test_css_241(self):
        self.LE.init_runner('test_css_240')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-082.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_240")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_241')

    def test_css_242(self):
        self.LE.init_runner('test_css_242')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-083.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_241")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_242')

    def test_css_243(self):
        self.LE.init_runner('test_css_243')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-084.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_242")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_243')

    def test_css_244(self):
        self.LE.init_runner('test_css_244')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-085.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_243")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_244')

    def test_css_245(self):
        self.LE.init_runner('test_css_245')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-086.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_244")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_245')

    def test_css_246(self):
        self.LE.init_runner('test_css_246')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-087.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_245")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_246')

    def test_css_247(self):
        self.LE.init_runner('test_css_247')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-088.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_246")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_247')

    def test_css_248(self):
        self.LE.init_runner('test_css_248')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-089.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_247")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_248')

    def test_css_249(self):
        self.LE.init_runner('test_css_249')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-090.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_248")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_249')

    def test_css_250(self):
        self.LE.init_runner('test_css_250')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-091.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_249")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_250')

    def test_css_251(self):
        self.LE.init_runner('test_css_251')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-092.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_250")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_251')

    def test_css_252(self):
        self.LE.init_runner('test_css_252')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-093.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_251")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_252')

    def test_css_253(self):
        self.LE.init_runner('test_css_253')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-094.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_252")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_253')

    def test_css_254(self):
        self.LE.init_runner('test_css_254')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-095.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_253")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_254')

    def test_css_255(self):
        self.LE.init_runner('test_css_255')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-096.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_254")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_255')

    def test_css_256(self):
        self.LE.init_runner('test_css_256')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-097.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_255")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_256')

    def test_css_257(self):
        self.LE.init_runner('test_css_257')  # ��runnerҳ��
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-098.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_256")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_257')

    def test_css_258(self):
        self.LE.init_runner('test_css_258')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-099.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_257")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_258')

    def test_css_259(self):
        self.LE.init_runner('test_css_259')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-100.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_258")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_259')

    def test_css_260(self):
        self.LE.init_runner('test_css_260')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-101.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_259")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_260')

    def test_css_261(self):
        self.LE.init_runner('test_css_261')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-102.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_260")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_261')

    def test_css_262(self):
        self.LE.init_runner('test_css_262')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-103.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_261")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_262')

    def test_css_263(self):
        self.LE.init_runner('test_css_263')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-104.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_262")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_263')

    def test_css_264(self):
        self.LE.init_runner('test_css_264')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-105.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_263")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_264')

    def test_css_265(self):
        self.LE.init_runner('test_css_265')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-106.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_264")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_265')

    def test_css_266(self):
        self.LE.init_runner('test_css_266')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-107.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_265")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_266')

    def test_css_267(self):
        self.LE.init_runner('test_css_267')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-108.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_266")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_267')

    def test_css_268(self):
        self.LE.init_runner('test_css_268')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-109.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_267")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_268')

    def test_css_269(self):
        self.LE.init_runner('test_css_269')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-110.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_268")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_269')

    def test_css_270(self):
        self.LE.init_runner('test_css_270')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-111.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_269")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_270')

    def test_css_271(self):
        self.LE.init_runner('test_css_271')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-112.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_270")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_271')

    def test_css_272(self):
        self.LE.init_runner('test_css_272')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-113.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_271")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_272')

    def test_css_273(self):
        self.LE.init_runner('test_css_273')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-114.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_272")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_273')

    def test_css_274(self):
        self.LE.init_runner('test_css_274')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-115.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_273")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_274')

    def test_css_275(self):
        self.LE.init_runner('test_css_275')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-116.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_274")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_275')

    def test_css_276(self):
        self.LE.init_runner('test_css_276')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-117.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_275")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_276')

    def test_css_277(self):
        self.LE.init_runner('test_css_277')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-118.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_276")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_277')

    def test_css_278(self):
        self.LE.init_runner('test_css_278')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-119.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_277")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_278')

    def test_css_279(self):
        self.LE.init_runner('test_css_279')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-120.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_278")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_279')

    def test_css_280(self):
        self.LE.init_runner('test_css_280')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-121.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_279")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_280')

    def test_css_281(self):
        self.LE.init_runner('test_css_281')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-122.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_280")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_281')

    def test_css_282(self):
        self.LE.init_runner('test_css_282')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-123.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_281")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_282')

    def test_css_283(self):
        self.LE.init_runner('test_css_283')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-124.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_282")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_283')

    def test_css_284(self):
        self.LE.init_runner('test_css_284')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-125.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_283")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_284')

    def test_css_285(self):
        self.LE.init_runner('test_css_285')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-126.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_284")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_285')

    def test_css_286(self):
        self.LE.init_runner('test_css_286')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-127.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_285")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_286')

    def test_css_287(self):
        self.LE.init_runner('test_css_287')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-128.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_286")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_287')

    def test_css_288(self):
        self.LE.init_runner('test_css_288')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-129.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_287")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_288')

    def test_css_289(self):
        self.LE.init_runner('test_css_289')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-130.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_288")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_289')

    def test_css_290(self):
        self.LE.init_runner('test_css_290')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-131.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_289")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_290')

    def test_css_291(self):
        self.LE.init_runner('test_css_291')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-132.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_290")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_291')

    def test_css_292(self):
        self.LE.init_runner('test_css_292')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-133.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_291")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_292')

    def test_css_293(self):
        self.LE.init_runner('test_css_293')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-134.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_292")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_293')

    def test_css_294(self):
        self.LE.init_runner('test_css_294')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-135.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_293")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_294')

    def test_css_295(self):
        self.LE.init_runner('test_css_295')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-136.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_294")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_295')

    def test_css_296(self):
        self.LE.init_runner('test_css_296')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-137.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_295")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_296')

    def test_css_297(self):
        self.LE.init_runner('test_css_297')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-138.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_296")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_297')

    def test_css_298(self):
        self.LE.init_runner('test_css_298')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-139.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_297")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_298')

    def test_css_299(self):
        self.LE.init_runner('test_css_299')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-140.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_298")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_299')

    def test_css_300(self):
        self.LE.init_runner('test_css_300')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-141.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_299")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_300')

    def test_css_301(self):
        self.LE.init_runner('test_css_301')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-142.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_300")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_301')

    def test_css_302(self):
        self.LE.init_runner('test_css_302')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-143.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_301")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_302')

    def test_css_303(self):
        self.LE.init_runner('test_css_303')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-144.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_302")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_303')

    def test_css_304(self):
        self.LE.init_runner('test_css_304')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-145.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_303")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_304')

    def test_css_305(self):
        self.LE.init_runner('test_css_305')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-174.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_304")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_305')

    def test_css_306(self):
        self.LE.init_runner('test_css_306')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-175.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_305")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_306')

    def test_css_307(self):
        self.LE.init_runner('test_css_307')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-applies-to-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_306")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_307')

    def test_css_308(self):
        self.LE.init_runner('test_css_308')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-applies-to-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_307")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_308')

    def test_css_309(self):
        self.LE.init_runner('test_css_309')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-applies-to-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_308")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_309')

    def test_css_310(self):
        self.LE.init_runner('test_css_310')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-applies-to-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_309")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_310')

    def test_css_311(self):
        self.LE.init_runner('test_css_311')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-applies-to-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_310")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_311')

    def test_css_312(self):
        self.LE.init_runner('test_css_312')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-applies-to-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_311")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_312')

    def test_css_313(self):
        self.LE.init_runner('test_css_313')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-applies-to-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_312")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_313')

    def test_css_314(self):
        self.LE.init_runner('test_css_314')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-applies-to-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_313")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_314')

    def test_css_315(self):
        self.LE.init_runner('test_css_315')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-applies-to-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_314")
        self.LE.test_implicit_expression_screenshot('//*[@id="inline-block"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_315')

    def test_css_316(self):
        self.LE.init_runner('test_css_316')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-applies-to-013.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_315")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_316')

    def test_css_317(self):
        self.LE.init_runner('test_css_317')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-applies-to-014.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_316")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_317')

    def test_css_318(self):
        self.LE.init_runner('test_css_318')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-color-applies-to-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_317")
        self.LE.test_implicit_expression_screenshot('//*[@id="caption"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_318')

    def test_css_319(self):
        self.LE.init_runner('test_css_319')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_318")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_319')

    def test_css_320(self):
        self.LE.init_runner('test_css_320')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_319")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_320')

    def test_css_321(self):
        self.LE.init_runner('test_css_321')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_320")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_321')

    def test_css_322(self):
        self.LE.init_runner('test_css_322')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_321")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_322')

    def test_css_323(self):
        self.LE.init_runner('test_css_323')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-applies-to-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_322")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_323')

    def test_css_324(self):
        self.LE.init_runner('test_css_324')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-applies-to-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_323")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_324')

    def test_css_325(self):
        self.LE.init_runner('test_css_325')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-applies-to-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_324")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_325')

    def test_css_326(self):
        self.LE.init_runner('test_css_326')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-applies-to-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_325")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_326')

    def test_css_327(self):
        self.LE.init_runner('test_css_327')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-applies-to-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_326")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_327')

    def test_css_328(self):
        self.LE.init_runner('test_css_328')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-applies-to-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_327")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_328')

    def test_css_329(self):
        self.LE.init_runner('test_css_329')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-applies-to-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_328")
        self.LE.test_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_329')

    def test_css_330(self):
        self.LE.init_runner('test_css_330')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-applies-to-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_329")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_330')

    def test_css_331(self):
        self.LE.init_runner('test_css_331')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-applies-to-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_330")
        self.LE.test_implicit_expression_screenshot('//*[@id="inline-block"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_331')

    def test_css_332(self):
        self.LE.init_runner('test_css_332')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-applies-to-013.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_331")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_332')

    def test_css_333(self):
        self.LE.init_runner('test_css_333')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-applies-to-014.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_332")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_333')

    def test_css_334(self):
        self.LE.init_runner('test_css_334')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-applies-to-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_333")
        self.LE.test_screenshot('//*[@id="caption"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_334')

    def test_css_335(self):
        self.LE.init_runner('test_css_335')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-cover-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_334")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_335')

    def test_css_336(self):
        self.LE.init_runner('test_css_336')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-cover-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_335")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_336')

    def test_css_337(self):
        self.LE.init_runner('test_css_337')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-cover-attachment-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_336")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_337')

    def test_css_338(self):
        self.LE.init_runner('test_css_338')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-image-transparency-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_337")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_338')

    def test_css_339(self):
        self.LE.init_runner('test_css_339')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-intrinsic-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_338")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_339')

    def test_css_340(self):
        self.LE.init_runner('test_css_340')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-intrinsic-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_339")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_340')

    def test_css_341(self):
        self.LE.init_runner('test_css_341')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-intrinsic-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_340")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_341')

    def test_css_342(self):
        self.LE.init_runner('test_css_342')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-intrinsic-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_341")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_342')

    def test_css_343(self):
        self.LE.init_runner('test_css_343')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-intrinsic-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_342")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_343')

    def test_css_344(self):
        self.LE.init_runner('test_css_344')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-intrinsic-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_343")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_344')

    def test_css_345(self):
        self.LE.init_runner('test_css_345')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-intrinsic-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_344")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_345')

    def test_css_346(self):
        self.LE.init_runner('test_css_346')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-intrinsic-008.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_345")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_346')

    def test_css_347(self):
        self.LE.init_runner('test_css_347')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-intrinsic-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_346")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_347')

    def test_css_348(self):
        self.LE.init_runner('test_css_348')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-intrinsic-010.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_347")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_348')

    def test_css_349(self):
        self.LE.init_runner('test_css_349')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_348")
        self.LE.test_implicit_expression_screenshot('//*[@id="expected-results"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_implicit_expression_screenshot('//*[@id="expected-results"]', "ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_349')

    def test_css_350(self):
        self.LE.init_runner('test_css_350')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_349")
        self.LE.test_implicit_expression_screenshot('//*[@id="expected-results"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_screenshot('//*[@id="expected-results"]', "ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_350')

    def test_css_351(self):
        self.LE.init_runner('test_css_351')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_350")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_351')

    def test_css_352(self):
        self.LE.init_runner('test_css_352')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_351")
        self.LE.test_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_352')

    def test_css_353(self):
        self.LE.init_runner('test_css_353')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_352")
        self.LE.test_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_353')

    def test_css_354(self):
        self.LE.init_runner('test_css_354')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_353")
        self.LE.test_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_354')

    def test_css_355(self):
        self.LE.init_runner('test_css_355')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-008.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_354")
        self.LE.test_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_355')

    def test_css_356(self):
        self.LE.init_runner('test_css_356')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-016.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_355")
        self.LE.test_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_356')

    def test_css_357(self):
        self.LE.init_runner('test_css_357')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-017.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_356")
        self.LE.test_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_357')

    def test_css_358(self):
        self.LE.init_runner('test_css_358')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-018.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_357")
        self.LE.test_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_358')

    def test_css_359(self):
        self.LE.init_runner('test_css_359')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-028.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_358")
        self.LE.test_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_359')

    def test_css_360(self):
        self.LE.init_runner('test_css_360')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-029.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_359")
        self.LE.test_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_360')

    def test_css_361(self):
        self.LE.init_runner('test_css_361')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-030.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_360")
        self.LE.test_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_361')

    def test_css_362(self):
        self.LE.init_runner('test_css_362')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-040.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_361")
        self.LE.test_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_362')

    def test_css_363(self):
        self.LE.init_runner('test_css_363')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-041.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_362")
        self.LE.test_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_363')

    def test_css_364(self):
        self.LE.init_runner('test_css_364')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-042.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_363")
        self.LE.test_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_364')

    def test_css_365(self):
        self.LE.init_runner('test_css_365')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-052.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_364")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_365')

    def test_css_366(self):
        self.LE.init_runner('test_css_366')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-053.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_365")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_366')

    def test_css_367(self):
        self.LE.init_runner('test_css_367')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-054.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_366")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_367')

    def test_css_368(self):
        self.LE.init_runner('test_css_368')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-064.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_367")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_368')

    def test_css_369(self):
        self.LE.init_runner('test_css_369')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-065.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_368")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_369')

    def test_css_370(self):
        self.LE.init_runner('test_css_370')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-066.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_369")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_370')

    def test_css_371(self):
        self.LE.init_runner('test_css_371')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-076.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_370")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_371')

    def test_css_372(self):
        self.LE.init_runner('test_css_372')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-077.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_371")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_372')

    def test_css_373(self):
        self.LE.init_runner('test_css_373')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-078.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_372")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_373')

    def test_css_374(self):
        self.LE.init_runner('test_css_374')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-088.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_373")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_374')

    def test_css_375(self):
        self.LE.init_runner('test_css_375')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-089.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_374")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_375')

    def test_css_376(self):
        self.LE.init_runner('test_css_376')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-090.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_375")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_376')

    def test_css_377(self):
        self.LE.init_runner('test_css_377')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-100.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_376")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_377')

    def test_css_378(self):
        self.LE.init_runner('test_css_378')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-101.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_377")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_378')

    def test_css_379(self):
        self.LE.init_runner('test_css_379')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-102.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_378")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_379')

    def test_css_380(self):
        self.LE.init_runner('test_css_380')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-109.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_379")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_380')

    def test_css_381(self):
        self.LE.init_runner('test_css_381')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-110.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_380")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_381')

    def test_css_382(self):
        self.LE.init_runner('test_css_382')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-111.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_381")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_382')

    def test_css_383(self):
        self.LE.init_runner('test_css_383')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-112.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_382")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_383')

    def test_css_384(self):
        self.LE.init_runner('test_css_384')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-113.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_383")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_384')

    def test_css_385(self):
        self.LE.init_runner('test_css_385')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-114.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_384")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_385')

    def test_css_386(self):
        self.LE.init_runner('test_css_386')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-115.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_385")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_386')

    def test_css_387(self):
        self.LE.init_runner('test_css_387')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-116.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_386")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_387')

    def test_css_388(self):
        self.LE.init_runner('test_css_388')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-117.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_387")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_388')

    def test_css_389(self):
        self.LE.init_runner('test_css_389')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-118.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_388")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_389')

    def test_css_390(self):
        self.LE.init_runner('test_css_390')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-119.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_389")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_390')

    def test_css_391(self):
        self.LE.init_runner('test_css_391')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-120.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_390")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_391')

    def test_css_392(self):
        self.LE.init_runner('test_css_392')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-121.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_391")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_392')

    def test_css_393(self):
        self.LE.init_runner('test_css_393')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-122.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_392")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_393')

    def test_css_394(self):
        self.LE.init_runner('test_css_394')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-123.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_393")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_394')

    def test_css_395(self):
        self.LE.init_runner('test_css_395')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-124.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_394")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_395')

    def test_css_396(self):
        self.LE.init_runner('test_css_396')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-125.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_395")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_396')

    def test_css_397(self):
        self.LE.init_runner('test_css_397')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-126.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_396")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_397')

    def test_css_398(self):
        self.LE.init_runner('test_css_398')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-127.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_397")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_398')

    def test_css_399(self):
        self.LE.init_runner('test_css_399')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-128.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_398")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_399')

    def test_css_400(self):
        self.LE.init_runner('test_css_400')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-129.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_399")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_400')

    def test_css_401(self):
        self.LE.init_runner('test_css_401')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-130.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_400")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_401')

    def test_css_402(self):
        self.LE.init_runner('test_css_402')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-131.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_401")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_402')

    def test_css_403(self):
        self.LE.init_runner('test_css_403')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-132.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_402")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_403')

    def test_css_404(self):
        self.LE.init_runner('test_css_404')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-133.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_403")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_404')

    def test_css_405(self):
        self.LE.init_runner('test_css_405')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-134.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_404")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_405')

    def test_css_406(self):
        self.LE.init_runner('test_css_406')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-135.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_405")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_406')

    def test_css_407(self):
        self.LE.init_runner('test_css_407')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-136.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_406")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_407')

    def test_css_408(self):
        self.LE.init_runner('test_css_408')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-137.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_407")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_408')

    def test_css_409(self):
        self.LE.init_runner('test_css_409')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-138.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_408")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_409')

    def test_css_410(self):
        self.LE.init_runner('test_css_410')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-139.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_409")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_410')

    def test_css_411(self):
        self.LE.init_runner('test_css_411')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-140.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_410")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_411')

    def test_css_412(self):
        self.LE.init_runner('test_css_412')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-141.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_411")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_412')

    def test_css_413(self):
        self.LE.init_runner('test_css_413')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-142.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_412")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_413')

    def test_css_414(self):
        self.LE.init_runner('test_css_414')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-143.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_413")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_414')

    def test_css_415(self):
        self.LE.init_runner('test_css_415')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-144.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_414")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_415')

    def test_css_416(self):
        self.LE.init_runner('test_css_416')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-145.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_415")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_416')

    def test_css_417(self):
        self.LE.init_runner('test_css_417')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-146.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_416")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_417')

    def test_css_418(self):
        self.LE.init_runner('test_css_418')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-147.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_417")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_418')

    def test_css_419(self):
        self.LE.init_runner('test_css_419')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-148.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_418")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_419')

    def test_css_420(self):
        self.LE.init_runner('test_css_420')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-149.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_419")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_420')

    def test_css_421(self):
        self.LE.init_runner('test_css_421')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-150.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_420")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_421')

    def test_css_422(self):
        self.LE.init_runner('test_css_422')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-151.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_421")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_422')

    def test_css_423(self):
        self.LE.init_runner('test_css_423')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-152.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_422")
        self.LE.test_implicit_expression_screenshot('//*[@id="nearest-positioned-ancestor"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_423')

    def test_css_424(self):
        self.LE.init_runner('test_css_424')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_423")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_424')

    def test_css_425(self):
        self.LE.init_runner('test_css_425')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-001a.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_424")
        self.LE.test_file_screenshot("test")  # referenceҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_425')

    def test_css_426(self):
        self.LE.init_runner('test_css_426')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-001b.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_425")
        self.LE.test_file_screenshot("test")  # referenceҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_426')

    def test_css_427(self):
        self.LE.init_runner('test_css_427')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-001c.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_426")
        self.LE.test_file_screenshot("test")  # referenceҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_427')

    def test_css_428(self):
        self.LE.init_runner('test_css_428')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-001d.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_427")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_428')

    def test_css_429(self):
        self.LE.init_runner('test_css_429')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-001e.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_428")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_429')

    def test_css_430(self):
        self.LE.init_runner('test_css_430')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_429")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_430')

    def test_css_431(self):
        self.LE.init_runner('test_css_431')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-002a.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_430")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_431')

    def test_css_432(self):
        self.LE.init_runner('test_css_432')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-002b.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_431")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_432')

    def test_css_433(self):
        self.LE.init_runner('test_css_433')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-002c.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_432")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_433')

    def test_css_434(self):
        self.LE.init_runner('test_css_434')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-002d.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_433")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_434')

    def test_css_435(self):
        self.LE.init_runner('test_css_435')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-002e.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_434")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_435')

    def test_css_436(self):
        self.LE.init_runner('test_css_436')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_435")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_436')

    def test_css_437(self):
        self.LE.init_runner('test_css_437')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-003b.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_436")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_437')

    def test_css_438(self):
        self.LE.init_runner('test_css_438')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-003c.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_437")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_438')

    def test_css_439(self):
        self.LE.init_runner('test_css_439')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-003d.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_438")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_439')

    def test_css_440(self):
        self.LE.init_runner('test_css_440')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-003e.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_439")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_440')

    def test_css_441(self):
        self.LE.init_runner('test_css_441')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_440")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_441')

    def test_css_442(self):
        self.LE.init_runner('test_css_442')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_441")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_442')

    def test_css_443(self):
        self.LE.init_runner('test_css_443')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-005a.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_442")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_443')

    def test_css_444(self):
        self.LE.init_runner('test_css_444')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-005b.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_443")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_444')

    def test_css_445(self):
        self.LE.init_runner('test_css_445')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-005c.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_444")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_445')

    def test_css_446(self):
        self.LE.init_runner('test_css_446')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-005d.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_445")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_446')

    def test_css_447(self):
        self.LE.init_runner('test_css_447')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-005e.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_446")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_447')

    def test_css_448(self):
        self.LE.init_runner('test_css_448')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_447")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_448')

    def test_css_449(self):
        self.LE.init_runner('test_css_449')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-006a.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_448")
        self.LE.test_implicit_expression_screenshot('//*[@id="tested-col"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_449')

    def test_css_450(self):
        self.LE.init_runner('test_css_450')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-006b.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_449")
        self.LE.test_implicit_expression_screenshot('//*[@id="tested-col"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_450')

    def test_css_451(self):
        self.LE.init_runner('test_css_451')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-006c.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_450")
        self.LE.test_screenshot('//*[@id="tested-col"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_451')

    def test_css_452(self):
        self.LE.init_runner('test_css_452')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-006d.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_451")
        self.LE.test_screenshot('//*[@id="tbody"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_452')

    def test_css_453(self):
        self.LE.init_runner('test_css_453')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-006e.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_452")
        self.LE.test_screenshot('//*[@id="tested-col"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_453')

    def test_css_454(self):
        self.LE.init_runner('test_css_454')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_453")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_454')

    def test_css_455(self):
        self.LE.init_runner('test_css_455')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_454")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_455')

    def test_css_456(self):
        self.LE.init_runner('test_css_456')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_455")
        self.LE.test_screenshot('//*[@id="inline-block"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_456')

    def test_css_457(self):
        self.LE.init_runner('test_css_457')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-013.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_456")
        self.LE.test_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_457')

    def test_css_458(self):
        self.LE.init_runner('test_css_458')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-013d.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_457")
        self.LE.test_screenshot('//*[@id="green-overlapping"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_458')

    def test_css_459(self):
        self.LE.init_runner('test_css_459')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-013e.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_458")
        self.LE.test_screenshot('//*[@id="overlapping-green"]', "test")  # testҳ���ͼ
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_459')

    def test_css_460(self):
        self.LE.init_runner('test_css_460')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-014.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_459")
        self.LE.test_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_460')

    def test_css_461(self):
        self.LE.init_runner('test_css_461')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-position-applies-to-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_460")
        self.LE.test_screenshot('//*[@id="row"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_461')

    def test_css_462(self):
        self.LE.init_runner('test_css_462')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-repeat-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_461")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_462')

    def test_css_463(self):
        self.LE.init_runner('test_css_463')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-repeat-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_462")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_463')

    def test_css_464(self):
        self.LE.init_runner('test_css_464')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-repeat-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_463")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_464')

    def test_css_465(self):
        self.LE.init_runner('test_css_465')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-repeat-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_464")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_465')

    def test_css_466(self):
        self.LE.init_runner('test_css_466')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-repeat-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_465")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_466')

    def test_css_467(self):
        self.LE.init_runner('test_css_467')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-repeat-applies-to-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_466")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_467')

    def test_css_468(self):
        self.LE.init_runner('test_css_468')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-repeat-applies-to-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_467")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_468')

    def test_css_469(self):
        self.LE.init_runner('test_css_469')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-repeat-applies-to-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_468")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_469')

    def test_css_470(self):
        self.LE.init_runner('test_css_470')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-repeat-applies-to-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_469")
        self.LE.test_screenshot('//*[@id="row"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_470')

    def test_css_471(self):
        self.LE.init_runner('test_css_471')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-repeat-applies-to-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_470")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_471')

    def test_css_472(self):
        self.LE.init_runner('test_css_472')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-repeat-applies-to-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_471")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_472')

    def test_css_473(self):
        self.LE.init_runner('test_css_473')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-repeat-applies-to-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_472")
        self.LE.test_screenshot('//*[@id="row"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_473')

    def test_css_474(self):
        self.LE.init_runner('test_css_474')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-repeat-applies-to-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_473")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_474')

    def test_css_475(self):
        self.LE.init_runner('test_css_475')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-repeat-applies-to-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_474")
        self.LE.test_screenshot('//*[@id="inline-block"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_475')

    def test_css_476(self):
        self.LE.init_runner('test_css_476')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-repeat-applies-to-013.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_475")
        self.LE.test_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_476')

    def test_css_477(self):
        self.LE.init_runner('test_css_477')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-repeat-applies-to-014.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_476")
        self.LE.test_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_477')

    def test_css_478(self):
        self.LE.init_runner('test_css_478')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-repeat-applies-to-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_477")
        self.LE.test_screenshot('//*[@id="row"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_478')

    def test_css_479(self):
        self.LE.init_runner('test_css_479')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-reset-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_478")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_479')

    def test_css_480(self):
        self.LE.init_runner('test_css_480')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_479")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_480')

    def test_css_481(self):
        self.LE.init_runner('test_css_481')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_480")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_481')

    def test_css_482(self):
        self.LE.init_runner('test_css_482')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_481")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_482')

    def test_css_483(self):
        self.LE.init_runner('test_css_483')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_482")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_483')

    def test_css_484(self):
        self.LE.init_runner('test_css_484')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_483")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_484')

    def test_css_485(self):
        self.LE.init_runner('test_css_485')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_484")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_485')

    def test_css_486(self):
        self.LE.init_runner('test_css_486')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-008.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_485")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_486')

    def test_css_487(self):
        self.LE.init_runner('test_css_487')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_486")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_487')

    def test_css_488(self):
        self.LE.init_runner('test_css_488')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-010.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_487")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_488')

    def test_css_489(self):
        self.LE.init_runner('test_css_489')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-011.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_488")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_489')

    def test_css_490(self):
        self.LE.init_runner('test_css_490')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-012b.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_489")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_490')

    def test_css_491(self):
        self.LE.init_runner('test_css_491')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-013b.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_490")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_491')

    def test_css_492(self):
        self.LE.init_runner('test_css_492')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-014b.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_491")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_492')

    def test_css_493(self):
        self.LE.init_runner('test_css_493')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_492")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_493')

    def test_css_494(self):
        self.LE.init_runner('test_css_494')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-016.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_493")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_494')

    def test_css_495(self):
        self.LE.init_runner('test_css_495')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-017.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_494")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_495')

    def test_css_496(self):
        self.LE.init_runner('test_css_496')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-018.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_495")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_496')

    def test_css_497(self):
        self.LE.init_runner('test_css_497')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-019.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_496")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_497')

    def test_css_498(self):
        self.LE.init_runner('test_css_498')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-020.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_497")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_498')

    def test_css_499(self):
        self.LE.init_runner('test_css_499')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-023.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_498")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_499')

    def test_css_500(self):
        self.LE.init_runner('test_css_500')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-024.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_499")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_500')

    def test_css_501(self):
        self.LE.init_runner('test_css_501')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-101.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_500")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_501')

    def test_css_502(self):
        self.LE.init_runner('test_css_502')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-102.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_501")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_502')

    def test_css_503(self):
        self.LE.init_runner('test_css_503')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/backgrounds/background-root-103.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_502")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_503')

    def test_css_504(self):
        self.LE.init_runner('test_css_504')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_503")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_504')

    def test_css_505(self):
        self.LE.init_runner('test_css_505')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_504")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_505')

    def test_css_506(self):
        self.LE.init_runner('test_css_506')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_505")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_506')

    def test_css_507(self):
        self.LE.init_runner('test_css_507')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-008.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_506")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_507')

    def test_css_508(self):
        self.LE.init_runner('test_css_508')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_507")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_508')

    def test_css_509(self):
        self.LE.init_runner('test_css_509')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-010.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_508")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_509')

    def test_css_510(self):
        self.LE.init_runner('test_css_510')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_509")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_510')

    def test_css_511(self):
        self.LE.init_runner('test_css_511')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_510")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_511')

    def test_css_512(self):
        self.LE.init_runner('test_css_512')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_511")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_512')

    def test_css_513(self):
        self.LE.init_runner('test_css_513')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_512")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_513')

    def test_css_514(self):
        self.LE.init_runner('test_css_514')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-005a.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_513")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_514')

    def test_css_515(self):
        self.LE.init_runner('test_css_515')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-005b.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_514")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_515')

    def test_css_516(self):
        self.LE.init_runner('test_css_516')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-006a.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_515")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_516')

    def test_css_517(self):
        self.LE.init_runner('test_css_517')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-006b.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_516")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_517')

    def test_css_518(self):
        self.LE.init_runner('test_css_518')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-007a.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_517")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_518')

    def test_css_519(self):
        self.LE.init_runner('test_css_519')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-007b.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_518")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_519')

    def test_css_520(self):
        self.LE.init_runner('test_css_520')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-008a.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_519")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_520')

    def test_css_521(self):
        self.LE.init_runner('test_css_521')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-008b.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_520")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_521')

    def test_css_522(self):
        self.LE.init_runner('test_css_522')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-009a.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_521")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_522')

    def test_css_523(self):
        self.LE.init_runner('test_css_523')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-009b.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_522")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_523')

    def test_css_524(self):
        self.LE.init_runner('test_css_524')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-010a.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_523")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_524')

    def test_css_525(self):
        self.LE.init_runner('test_css_525')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-010b.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_524")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_525')

    def test_css_526(self):
        self.LE.init_runner('test_css_526')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-011.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_525")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_526')

    def test_css_527(self):
        self.LE.init_runner('test_css_527')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_526")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_527')

    def test_css_528(self):
        self.LE.init_runner('test_css_528')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_527")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_528')

    def test_css_529(self):
        self.LE.init_runner('test_css_529')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_528")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_529')

    def test_css_530(self):
        self.LE.init_runner('test_css_530')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_529")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_530')

    def test_css_531(self):
        self.LE.init_runner('test_css_531')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_530")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_531')

    def test_css_532(self):
        self.LE.init_runner('test_css_532')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_531")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_532')

    def test_css_533(self):
        self.LE.init_runner('test_css_533')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_532")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_533')

    def test_css_534(self):
        self.LE.init_runner('test_css_534')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-008.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_533")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_534')

    def test_css_535(self):
        self.LE.init_runner('test_css_535')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_534")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_535')

    def test_css_536(self):
        self.LE.init_runner('test_css_536')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-010.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_535")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_536')

    def test_css_537(self):
        self.LE.init_runner('test_css_537')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-011.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_536")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_537')

    def test_css_538(self):
        self.LE.init_runner('test_css_538')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_537")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_538')

    def test_css_539(self):
        self.LE.init_runner('test_css_539')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-013.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_538")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_539')

    def test_css_540(self):
        self.LE.init_runner('test_css_540')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-014.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_539")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_540')

    def test_css_541(self):
        self.LE.init_runner('test_css_541')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_540")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_541')

    def test_css_542(self):
        self.LE.init_runner('test_css_542')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-016.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_541")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_542')

    def test_css_543(self):
        self.LE.init_runner('test_css_543')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-017.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_542")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_543')

    def test_css_544(self):
        self.LE.init_runner('test_css_544')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-018.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_543")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_544')

    def test_css_545(self):
        self.LE.init_runner('test_css_545')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-019.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_544")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_545')

    def test_css_546(self):
        self.LE.init_runner('test_css_546')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-020.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_545")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_546')

    def test_css_547(self):
        self.LE.init_runner('test_css_547')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-021.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_546")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_547')

    def test_css_548(self):
        self.LE.init_runner('test_css_548')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-022.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_547")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_548')

    def test_css_549(self):
        self.LE.init_runner('test_css_549')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-023.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_548")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_549')

    def test_css_550(self):
        self.LE.init_runner('test_css_550')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-024.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_549")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_550')

    def test_css_551(self):
        self.LE.init_runner('test_css_551')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-025.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_550")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_551')

    def test_css_552(self):
        self.LE.init_runner('test_css_552')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-026.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_551")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_552')

    def test_css_553(self):
        self.LE.init_runner('test_css_553')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-027.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_552")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_553')

    def test_css_554(self):
        self.LE.init_runner('test_css_554')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-028.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_553")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_554')

    def test_css_555(self):
        self.LE.init_runner('test_css_555')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-029.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_554")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_555')

    def test_css_556(self):
        self.LE.init_runner('test_css_556')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-030.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_555")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_556')

    def test_css_557(self):
        self.LE.init_runner('test_css_557')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-031.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_556")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_557')

    def test_css_558(self):
        self.LE.init_runner('test_css_558')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-032.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_557")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_558')

    def test_css_559(self):
        self.LE.init_runner('test_css_559')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-033.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_558")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_559')

    def test_css_560(self):
        self.LE.init_runner('test_css_560')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-034.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_559")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_560')

    def test_css_561(self):
        self.LE.init_runner('test_css_561')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-035.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_560")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_561')

    def test_css_562(self):
        self.LE.init_runner('test_css_562')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-036.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_561")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_562')

    def test_css_563(self):
        self.LE.init_runner('test_css_563')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-037.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_562")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_563')

    def test_css_564(self):
        self.LE.init_runner('test_css_564')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-038.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_563")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_564')

    def test_css_565(self):
        self.LE.init_runner('test_css_565')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-039.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_564")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_565')

    def test_css_566(self):
        self.LE.init_runner('test_css_566')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-040.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_565")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_566')

    def test_css_567(self):
        self.LE.init_runner('test_css_567')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-041.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_566")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_567')

    def test_css_568(self):
        self.LE.init_runner('test_css_568')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-042.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_567")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_568')

    def test_css_569(self):
        self.LE.init_runner('test_css_569')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-043.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_568")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_569')

    def test_css_570(self):
        self.LE.init_runner('test_css_570')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-044.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_569")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_570')

    def test_css_571(self):
        self.LE.init_runner('test_css_571')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-box-model-045.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_570")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_571')

    def test_css_572(self):
        self.LE.init_runner('test_css_572')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-breaking-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_571")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_572')

    def test_css_573(self):
        self.LE.init_runner('test_css_573')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-breaking-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_572")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_573')

    def test_css_574(self):
        self.LE.init_runner('test_css_574')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-breaking-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_573")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_574')

    def test_css_575(self):
        self.LE.init_runner('test_css_575')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-glyph-mirroring-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_574")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_575')

    def test_css_576(self):
        self.LE.init_runner('test_css_576')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-glyph-mirroring-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_575")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_576')

    def test_css_577(self):
        self.LE.init_runner('test_css_577')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-inline-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_576")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_577')

    def test_css_578(self):
        self.LE.init_runner('test_css_578')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/bidi-inline-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_577")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_578')

    def test_css_579(self):
        self.LE.init_runner('test_css_579')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/direction-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_578")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_579')

    def test_css_580(self):
        self.LE.init_runner('test_css_580')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/direction-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_579")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_580')

    def test_css_581(self):
        self.LE.init_runner('test_css_581')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/direction-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_580")
        self.LE.test_implicit_expression_screenshot('//*[@id="wrapper"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_581')

    def test_css_582(self):
        self.LE.init_runner('test_css_582')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/direction-applies-to-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_581")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_582')

    def test_css_583(self):
        self.LE.init_runner('test_css_583')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/direction-applies-to-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_582")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_583')

    def test_css_584(self):
        self.LE.init_runner('test_css_584')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/direction-applies-to-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_583")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_584')

    def test_css_585(self):
        self.LE.init_runner('test_css_585')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/direction-applies-to-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_584")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_585')

    def test_css_586(self):
        self.LE.init_runner('test_css_586')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/direction-applies-to-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_585")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="row"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_586')

    def test_css_587(self):
        self.LE.init_runner('test_css_587')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/direction-applies-to-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_586")
        self.LE.test_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="row"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_587')

    def test_css_588(self):
        self.LE.init_runner('test_css_588')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/direction-applies-to-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_587")
        self.LE.test_implicit_expression_screenshot('//*[@id="row"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_588')

    def test_css_589(self):
        self.LE.init_runner('test_css_589')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/direction-applies-to-008.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_588")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_589')

    def test_css_590(self):
        self.LE.init_runner('test_css_590')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/direction-applies-to-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_589")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_590')

    def test_css_591(self):
        self.LE.init_runner('test_css_591')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/direction-applies-to-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_590")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_591')

    def test_css_592(self):
        self.LE.init_runner('test_css_592')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/direction-applies-to-013.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_591")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_592')

    def test_css_593(self):
        self.LE.init_runner('test_css_593')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/direction-applies-to-014.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_592")
        self.LE.test_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_593')

    def test_css_594(self):
        self.LE.init_runner('test_css_594')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/direction-applies-to-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_593")
        self.LE.test_screenshot('//*[@id="caption"]', "test")  # testҳ���ͼ
        self.LE.test_screenshot('//*[@id="row"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_594')

    def test_css_595(self):
        self.LE.init_runner('test_css_595')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/line-breaking-bidi-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_594")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_595')

    def test_css_596(self):
        self.LE.init_runner('test_css_596')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/line-breaking-bidi-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_595")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_596')

    def test_css_597(self):
        self.LE.init_runner('test_css_597')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/line-breaking-bidi-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_596")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_597')

    def test_css_598(self):
        self.LE.init_runner('test_css_598')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/unicode-bidi-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_597")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_598')

    def test_css_599(self):
        self.LE.init_runner('test_css_599')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/unicode-bidi-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_598")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_599')

    def test_css_600(self):
        self.LE.init_runner('test_css_600')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/unicode-bidi-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_599")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_600')

    def test_css_601(self):
        self.LE.init_runner('test_css_601')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/unicode-bidi-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_600")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_601')

    def test_css_602(self):
        self.LE.init_runner('test_css_602')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/unicode-bidi-applies-to-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_601")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_602')

    def test_css_603(self):
        self.LE.init_runner('test_css_603')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/unicode-bidi-applies-to-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_602")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_603')

    def test_css_604(self):
        self.LE.init_runner('test_css_604')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/unicode-bidi-applies-to-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_603")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_604')

    def test_css_605(self):
        self.LE.init_runner('test_css_605')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/unicode-bidi-applies-to-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_604")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_605')

    def test_css_606(self):
        self.LE.init_runner('test_css_606')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/unicode-bidi-applies-to-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_605")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_606')

    def test_css_607(self):
        self.LE.init_runner('test_css_607')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/unicode-bidi-applies-to-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_606")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_607')

    def test_css_608(self):
        self.LE.init_runner('test_css_608')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/unicode-bidi-applies-to-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_607")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_608')

    def test_css_609(self):
        self.LE.init_runner('test_css_609')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/unicode-bidi-applies-to-008.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_608")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_609')

    def test_css_610(self):
        self.LE.init_runner('test_css_610')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/unicode-bidi-applies-to-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_609")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_610')

    def test_css_611(self):
        self.LE.init_runner('test_css_611')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/unicode-bidi-applies-to-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_610")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_611')

    def test_css_612(self):
        self.LE.init_runner('test_css_612')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/unicode-bidi-applies-to-013.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_611")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_612')

    def test_css_613(self):
        self.LE.init_runner('test_css_613')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/unicode-bidi-applies-to-014.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_612")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_613')

    def test_css_614(self):
        self.LE.init_runner('test_css_614')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/bidi-text/unicode-bidi-applies-to-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_613")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="row"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_614')

    def test_css_615(self):
        self.LE.init_runner('test_css_615')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/border-seams-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_614")
        self.LE.test_implicit_expression_screenshot('//*[@id="outer"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_615')

    def test_css_616(self):
        self.LE.init_runner('test_css_616')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_615")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_616')

    def test_css_617(self):
        self.LE.init_runner('test_css_617')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_616")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_617')

    def test_css_618(self):
        self.LE.init_runner('test_css_618')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_617")
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_618')

    def test_css_619(self):
        self.LE.init_runner('test_css_619')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_618")
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_619')

    def test_css_620(self):
        self.LE.init_runner('test_css_620')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-008.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_619")
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_620')

    def test_css_621(self):
        self.LE.init_runner('test_css_621')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-applies-to-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_620")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_621')

    def test_css_622(self):
        self.LE.init_runner('test_css_622')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-applies-to-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_621")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_622')

    def test_css_623(self):
        self.LE.init_runner('test_css_623')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-applies-to-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_622")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_623')

    def test_css_624(self):
        self.LE.init_runner('test_css_624')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-applies-to-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_623")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_624')

    def test_css_625(self):
        self.LE.init_runner('test_css_625')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-applies-to-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_624")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_625')

    def test_css_626(self):
        self.LE.init_runner('test_css_626')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-applies-to-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_625")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_626')

    def test_css_627(self):
        self.LE.init_runner('test_css_627')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-applies-to-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_626")
        self.LE.test_implicit_expression_screenshot('//*[@id="cell"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_627')

    def test_css_628(self):
        self.LE.init_runner('test_css_628')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-applies-to-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_627")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_628')

    def test_css_629(self):
        self.LE.init_runner('test_css_629')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-applies-to-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_628")
        self.LE.test_implicit_expression_screenshot('//*[@id="inline-block"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_629')

    def test_css_630(self):
        self.LE.init_runner('test_css_630')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-applies-to-013.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_629")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_630')

    def test_css_631(self):
        self.LE.init_runner('test_css_631')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-applies-to-014.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_630")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_631')

    def test_css_632(self):
        self.LE.init_runner('test_css_632')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-applies-to-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_631")
        self.LE.test_implicit_expression_screenshot('//*[@id="caption"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="row"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_632')

    def test_css_633(self):
        self.LE.init_runner('test_css_633')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_632")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_633')

    def test_css_634(self):
        self.LE.init_runner('test_css_634')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_633")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_634')

    def test_css_635(self):
        self.LE.init_runner('test_css_635')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_634")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_635')

    def test_css_636(self):
        self.LE.init_runner('test_css_636')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-008.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_635")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_636')

    def test_css_637(self):
        self.LE.init_runner('test_css_637')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-016.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_636")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_637')

    def test_css_638(self):
        self.LE.init_runner('test_css_638')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-018.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_637")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_638')

    def test_css_639(self):
        self.LE.init_runner('test_css_639')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-applies-to-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_638")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_639')

    def test_css_640(self):
        self.LE.init_runner('test_css_640')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-applies-to-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_639")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_640')

    def test_css_641(self):
        self.LE.init_runner('test_css_641')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-applies-to-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_640")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_641')

    def test_css_642(self):
        self.LE.init_runner('test_css_642')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-applies-to-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_641")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_642')

    def test_css_643(self):
        self.LE.init_runner('test_css_643')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-applies-to-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_642")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_643')

    def test_css_644(self):
        self.LE.init_runner('test_css_644')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-applies-to-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_643")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_644')

    def test_css_645(self):
        self.LE.init_runner('test_css_645')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-applies-to-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_644")
        self.LE.test_implicit_expression_screenshot('//*[@id="cell"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_645')

    def test_css_646(self):
        self.LE.init_runner('test_css_646')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-applies-to-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_645")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_646')

    def test_css_647(self):
        self.LE.init_runner('test_css_647')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-applies-to-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_646")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_647')

    def test_css_648(self):
        self.LE.init_runner('test_css_648')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-applies-to-013.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_647")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_648')

    def test_css_649(self):
        self.LE.init_runner('test_css_649')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-applies-to-014.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_648")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_649')

    def test_css_650(self):
        self.LE.init_runner('test_css_650')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-applies-to-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_649")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="row"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_650')

    def test_css_651(self):
        self.LE.init_runner('test_css_651')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_650")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_651')

    def test_css_652(self):
        self.LE.init_runner('test_css_652')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_651")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_652')

    def test_css_653(self):
        self.LE.init_runner('test_css_653')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_652")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_653')

    def test_css_654(self):
        self.LE.init_runner('test_css_654')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_653")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_654')

    def test_css_655(self):
        self.LE.init_runner('test_css_655')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_654")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_655')

    def test_css_656(self):
        self.LE.init_runner('test_css_656')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_655")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_656')

    def test_css_657(self):
        self.LE.init_runner('test_css_657')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_656")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_657')

    def test_css_658(self):
        self.LE.init_runner('test_css_658')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-008.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_657")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_658')

    def test_css_659(self):
        self.LE.init_runner('test_css_659')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_658")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_659')

    def test_css_660(self):
        self.LE.init_runner('test_css_660')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-010.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_659")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_660')

    def test_css_661(self):
        self.LE.init_runner('test_css_661')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-011.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_660")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_661')

    def test_css_662(self):
        self.LE.init_runner('test_css_662')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_661")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_662')

    def test_css_663(self):
        self.LE.init_runner('test_css_663')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-013.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_662")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_663')

    def test_css_664(self):
        self.LE.init_runner('test_css_664')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-014.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_663")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_664')

    def test_css_665(self):
        self.LE.init_runner('test_css_665')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_664")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_665')

    def test_css_666(self):
        self.LE.init_runner('test_css_666')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-016.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_665")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_666')

    def test_css_667(self):
        self.LE.init_runner('test_css_667')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-017.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_666")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_667')

    def test_css_668(self):
        self.LE.init_runner('test_css_668')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-018.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_667")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_668')

    def test_css_669(self):
        self.LE.init_runner('test_css_669')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-019.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_668")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_669')

    def test_css_670(self):
        self.LE.init_runner('test_css_670')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-020.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_669")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_670')

    def test_css_671(self):
        self.LE.init_runner('test_css_671')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-021.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_670")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_671')

    def test_css_672(self):
        self.LE.init_runner('test_css_672')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-022.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_671")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_672')

    def test_css_673(self):
        self.LE.init_runner('test_css_673')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-023.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_672")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_673')

    def test_css_674(self):
        self.LE.init_runner('test_css_674')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-024.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_673")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_674')

    def test_css_675(self):
        self.LE.init_runner('test_css_675')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-025.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_674")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_675')

    def test_css_676(self):
        self.LE.init_runner('test_css_676')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-026.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_675")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_676')

    def test_css_677(self):
        self.LE.init_runner('test_css_677')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-027.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_676")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_677')

    def test_css_678(self):
        self.LE.init_runner('test_css_678')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-028.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_677")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_678')

    def test_css_679(self):
        self.LE.init_runner('test_css_679')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-029.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_678")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_679')

    def test_css_680(self):
        self.LE.init_runner('test_css_680')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-030.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_679")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_680')

    def test_css_681(self):
        self.LE.init_runner('test_css_681')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-031.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_680")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_681')

    def test_css_682(self):
        self.LE.init_runner('test_css_682')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-032.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_681")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_682')

    def test_css_683(self):
        self.LE.init_runner('test_css_683')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-033.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_682")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_683')

    def test_css_684(self):
        self.LE.init_runner('test_css_684')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-034.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_683")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_684')

    def test_css_685(self):
        self.LE.init_runner('test_css_685')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-035.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_684")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_685')

    def test_css_686(self):
        self.LE.init_runner('test_css_686')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-036.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_685")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_686')

    def test_css_687(self):
        self.LE.init_runner('test_css_687')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-037.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_686")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_687')

    def test_css_688(self):
        self.LE.init_runner('test_css_688')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-038.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_687")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_688')

    def test_css_689(self):
        self.LE.init_runner('test_css_689')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-039.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_688")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_689')

    def test_css_690(self):
        self.LE.init_runner('test_css_690')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-040.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_689")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_690')

    def test_css_691(self):
        self.LE.init_runner('test_css_691')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-041.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_690")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_691')

    def test_css_692(self):
        self.LE.init_runner('test_css_692')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-042.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_691")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_692')

    def test_css_693(self):
        self.LE.init_runner('test_css_693')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-043.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_692")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����

        self.LE.runner_end('test_css_693')

    def test_css_694(self):
        self.LE.init_runner('test_css_694')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-044.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_693")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_694')

    def test_css_695(self):
        self.LE.init_runner('test_css_695')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-045.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_694")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_695')

    def test_css_696(self):
        self.LE.init_runner('test_css_696')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-046.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_695")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_696')

    def test_css_697(self):
        self.LE.init_runner('test_css_697')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-047.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_696")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_697')

    def test_css_698(self):
        self.LE.init_runner('test_css_698')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-048.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_697")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_698')

    def test_css_699(self):
        self.LE.init_runner('test_css_699')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-049.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_698")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_699')

    def test_css_700(self):
        self.LE.init_runner('test_css_700')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-050.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_699")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_700')

    def test_css_701(self):
        self.LE.init_runner('test_css_701')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-051.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_700")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_701')

    def test_css_702(self):
        self.LE.init_runner('test_css_702')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-052.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_701")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_702')

    def test_css_703(self):
        self.LE.init_runner('test_css_703')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-053.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_702")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_703')

    def test_css_704(self):
        self.LE.init_runner('test_css_704')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-054.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_703")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_704')

    def test_css_705(self):
        self.LE.init_runner('test_css_705')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-055.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_704")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_705')

    def test_css_706(self):
        self.LE.init_runner('test_css_706')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-056.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_705")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_706')

    def test_css_707(self):
        self.LE.init_runner('test_css_707')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-057.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_706")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_707')

    def test_css_708(self):
        self.LE.init_runner('test_css_708')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-058.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_707")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_708')

    def test_css_709(self):
        self.LE.init_runner('test_css_709')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-059.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_708")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_709')

    def test_css_710(self):
        self.LE.init_runner('test_css_710')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-060.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_709")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_710')

    def test_css_711(self):
        self.LE.init_runner('test_css_711')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-061.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_710")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_711')

    def test_css_712(self):
        self.LE.init_runner('test_css_712')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-062.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_711")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_712')

    def test_css_713(self):
        self.LE.init_runner('test_css_713')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-063.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_712")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_713')

    def test_css_714(self):
        self.LE.init_runner('test_css_714')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-064.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_713")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_714')

    def test_css_715(self):
        self.LE.init_runner('test_css_715')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-065.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_714")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_715')

    def test_css_716(self):
        self.LE.init_runner('test_css_716')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-066.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_715")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_716')

    def test_css_717(self):
        self.LE.init_runner('test_css_717')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-067.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_716")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_717')

    def test_css_718(self):
        self.LE.init_runner('test_css_718')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-068.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_717")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_718')

    def test_css_719(self):
        self.LE.init_runner('test_css_719')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-069.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_718")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_719')

    def test_css_720(self):
        self.LE.init_runner('test_css_720')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-070.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_719")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_720')

    def test_css_721(self):
        self.LE.init_runner('test_css_721')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-071.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_720")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_721')

    def test_css_722(self):
        self.LE.init_runner('test_css_722')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-072.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_721")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_722')

    def test_css_723(self):
        self.LE.init_runner('test_css_723')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-073.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_722")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_723')

    def test_css_724(self):
        self.LE.init_runner('test_css_724')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-074.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_723")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_724')

    def test_css_725(self):
        self.LE.init_runner('test_css_725')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-075.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_724")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_725')

    def test_css_726(self):
        self.LE.init_runner('test_css_726')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-076.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_725")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_726')

    def test_css_727(self):
        self.LE.init_runner('test_css_727')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-077.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_726")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_727')

    def test_css_728(self):
        self.LE.init_runner('test_css_728')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-078.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_727")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_728')

    def test_css_729(self):
        self.LE.init_runner('test_css_729')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-079.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_728")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_729')

    def test_css_730(self):
        self.LE.init_runner('test_css_730')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-080.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_729")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_730')

    def test_css_731(self):
        self.LE.init_runner('test_css_731')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-081.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_730")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_731')

    def test_css_732(self):
        self.LE.init_runner('test_css_732')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-082.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_731")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_732')

    def test_css_733(self):
        self.LE.init_runner('test_css_733')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-083.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_732")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_733')

    def test_css_734(self):
        self.LE.init_runner('test_css_734')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-084.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_733")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_734')

    def test_css_735(self):
        self.LE.init_runner('test_css_735')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-085.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_734")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_735')

    def test_css_736(self):
        self.LE.init_runner('test_css_736')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-086.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_735")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_736')

    def test_css_737(self):
        self.LE.init_runner('test_css_737')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-087.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_736")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_737')

    def test_css_738(self):
        self.LE.init_runner('test_css_738')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-088.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_737")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_738')

    def test_css_739(self):
        self.LE.init_runner('test_css_739')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-089.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_738")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_739')

    def test_css_740(self):
        self.LE.init_runner('test_css_740')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-090.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_739")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_740')

    def test_css_741(self):
        self.LE.init_runner('test_css_741')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-091.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_740")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_741')

    def test_css_742(self):
        self.LE.init_runner('test_css_742')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-092.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_741")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_742')

    def test_css_743(self):
        self.LE.init_runner('test_css_743')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-093.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_742")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_743')

    def test_css_744(self):
        self.LE.init_runner('test_css_744')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-094.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_743")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_744')

    def test_css_745(self):
        self.LE.init_runner('test_css_745')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-095.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_744")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_745')

    def test_css_746(self):
        self.LE.init_runner('test_css_746')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-096.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_745")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_746')

    def test_css_747(self):
        self.LE.init_runner('test_css_747')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-097.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_746")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_747')

    def test_css_748(self):
        self.LE.init_runner('test_css_748')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-098.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_747")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_748')

    def test_css_749(self):
        self.LE.init_runner('test_css_749')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-099.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_748")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_749')

    def test_css_750(self):
        self.LE.init_runner('test_css_750')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-100.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_749")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_750')

    def test_css_751(self):
        self.LE.init_runner('test_css_751')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-101.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_750")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_751')

    def test_css_752(self):
        self.LE.init_runner('test_css_752')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-102.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_751")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_752')

    def test_css_753(self):
        self.LE.init_runner('test_css_753')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-103.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_752")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_753')

    def test_css_754(self):
        self.LE.init_runner('test_css_754')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-104.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_753")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_754')

    def test_css_755(self):
        self.LE.init_runner('test_css_755')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-105.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_754")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_755')

    def test_css_756(self):
        self.LE.init_runner('test_css_756')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-106.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_755")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_756')

    def test_css_757(self):
        self.LE.init_runner('test_css_757')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-107.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_756")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_757')

    def test_css_758(self):
        self.LE.init_runner('test_css_758')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-108.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_757")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_758')

    def test_css_759(self):
        self.LE.init_runner('test_css_759')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-109.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_758")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_759')

    def test_css_760(self):
        self.LE.init_runner('test_css_760')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-110.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_759")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_760')

    def test_css_761(self):
        self.LE.init_runner('test_css_761')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-111.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_760")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_761')

    def test_css_762(self):
        self.LE.init_runner('test_css_762')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-112.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_761")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_762')

    def test_css_763(self):
        self.LE.init_runner('test_css_763')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-113.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_762")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_763')

    def test_css_764(self):
        self.LE.init_runner('test_css_764')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-114.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_763")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_764')

    def test_css_765(self):
        self.LE.init_runner('test_css_765')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-115.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_764")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_765')

    def test_css_766(self):
        self.LE.init_runner('test_css_766')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-116.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_765")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_766')

    def test_css_767(self):
        self.LE.init_runner('test_css_767')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-117.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_766")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_767')

    def test_css_768(self):
        self.LE.init_runner('test_css_768')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-118.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_767")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_768')

    def test_css_769(self):
        self.LE.init_runner('test_css_769')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-119.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_768")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_769')

    def test_css_770(self):
        self.LE.init_runner('test_css_770')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-120.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_769")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_770')

    def test_css_771(self):
        self.LE.init_runner('test_css_771')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-121.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_770")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_771')

    def test_css_772(self):
        self.LE.init_runner('test_css_772')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-122.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_771")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_772')

    def test_css_773(self):
        self.LE.init_runner('test_css_773')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-123.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_772")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_773')

    def test_css_774(self):
        self.LE.init_runner('test_css_774')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-124.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_773")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_774')

    def test_css_775(self):
        self.LE.init_runner('test_css_775')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-125.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_774")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_775')

    def test_css_776(self):
        self.LE.init_runner('test_css_776')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-126.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_775")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_776')

    def test_css_777(self):
        self.LE.init_runner('test_css_777')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-127.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_776")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_777')

    def test_css_778(self):
        self.LE.init_runner('test_css_778')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-128.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_777")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_778')

    def test_css_779(self):
        self.LE.init_runner('test_css_779')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-129.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_778")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_779')

    def test_css_780(self):
        self.LE.init_runner('test_css_780')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-130.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_779")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_780')

    def test_css_781(self):
        self.LE.init_runner('test_css_781')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-131.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_780")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_781')

    def test_css_782(self):
        self.LE.init_runner('test_css_782')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-132.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_781")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_782')

    def test_css_783(self):
        self.LE.init_runner('test_css_783')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-133.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_782")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_783')

    def test_css_784(self):
        self.LE.init_runner('test_css_784')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-134.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_783")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_784')

    def test_css_785(self):
        self.LE.init_runner('test_css_785')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-135.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_784")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_785')

    def test_css_786(self):
        self.LE.init_runner('test_css_786')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-136.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_785")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_786')

    def test_css_787(self):
        self.LE.init_runner('test_css_787')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-137.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_786")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_787')

    def test_css_788(self):
        self.LE.init_runner('test_css_788')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-138.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_787")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_788')

    def test_css_789(self):
        self.LE.init_runner('test_css_789')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-139.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_788")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_789')

    def test_css_790(self):
        self.LE.init_runner('test_css_790')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-140.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_789")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_790')

    def test_css_791(self):
        self.LE.init_runner('test_css_791')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-141.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_790")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_791')

    def test_css_792(self):
        self.LE.init_runner('test_css_792')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-142.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_791")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_792')

    def test_css_793(self):
        self.LE.init_runner('test_css_793')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-143.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_792")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_793')

    def test_css_794(self):
        self.LE.init_runner('test_css_794')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-144.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_793")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_794')

    def test_css_795(self):
        self.LE.init_runner('test_css_795')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-145.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_794")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_795')

    def test_css_796(self):
        self.LE.init_runner('test_css_796')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-174.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_795")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_796')

    def test_css_797(self):
        self.LE.init_runner('test_css_797')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-175.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_796")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_797')

    def test_css_798(self):
        self.LE.init_runner('test_css_798')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-applies-to-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_797")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_798')

    def test_css_799(self):
        self.LE.init_runner('test_css_799')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-applies-to-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_798")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_799')

    def test_css_800(self):
        self.LE.init_runner('test_css_800')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-applies-to-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_799")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_800')

    def test_css_801(self):
        self.LE.init_runner('test_css_801')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-applies-to-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_800")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_801')

    def test_css_802(self):
        self.LE.init_runner('test_css_802')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-applies-to-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_801")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_802')

    def test_css_803(self):
        self.LE.init_runner('test_css_803')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-applies-to-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_802")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_803')

    def test_css_804(self):
        self.LE.init_runner('test_css_804')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-applies-to-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_803")
        self.LE.test_implicit_expression_screenshot('//*[@id="cell"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_804')

    def test_css_805(self):
        self.LE.init_runner('test_css_805')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-applies-to-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_804")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_805')

    def test_css_806(self):
        self.LE.init_runner('test_css_806')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-applies-to-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_805")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_806')

    def test_css_807(self):
        self.LE.init_runner('test_css_807')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-applies-to-013.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_806")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_807')

    def test_css_808(self):
        self.LE.init_runner('test_css_808')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-applies-to-014.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_807")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_808')

    def test_css_809(self):
        self.LE.init_runner('test_css_809')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-color-applies-to-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_808")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="row"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_809')

    def test_css_810(self):
        self.LE.init_runner('test_css_810')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-style-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_809")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_810')

    def test_css_811(self):
        self.LE.init_runner('test_css_811')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-style-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_810")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_811')

    def test_css_812(self):
        self.LE.init_runner('test_css_812')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-style-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_811")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_812')

    def test_css_813(self):
        self.LE.init_runner('test_css_813')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_812")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_813')

    def test_css_814(self):
        self.LE.init_runner('test_css_814')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_813")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_814')

    def test_css_815(self):
        self.LE.init_runner('test_css_815')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_814")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_815')

    def test_css_816(self):
        self.LE.init_runner('test_css_816')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_815")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_816')

    def test_css_817(self):
        self.LE.init_runner('test_css_817')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_816")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_817')

    def test_css_818(self):
        self.LE.init_runner('test_css_818')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_817")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_818')

    def test_css_819(self):
        self.LE.init_runner('test_css_819')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_818")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_819')

    def test_css_820(self):
        self.LE.init_runner('test_css_820')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_819")
        self.LE.test_implicit_expression_screenshot('//*[@id="span1"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="span2"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_820')

    def test_css_821(self):
        self.LE.init_runner('test_css_821')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-013.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_820")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_821')

    def test_css_822(self):
        self.LE.init_runner('test_css_822')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_821")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_822')

    def test_css_823(self):
        self.LE.init_runner('test_css_823')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-016.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_822")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_823')

    def test_css_824(self):
        self.LE.init_runner('test_css_824')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-017.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_823")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_824')

    def test_css_825(self):
        self.LE.init_runner('test_css_825')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-018.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_824")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_825')

    def test_css_826(self):
        self.LE.init_runner('test_css_826')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-023.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_825")
        self.LE.test_implicit_expression_screenshot('//*[@id="span1"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="span2"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_826')

    def test_css_827(self):
        self.LE.init_runner('test_css_827')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-024.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_826")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_827')

    def test_css_828(self):
        self.LE.init_runner('test_css_828')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-025.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_827")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_828')

    def test_css_829(self):
        self.LE.init_runner('test_css_829')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-026.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_828")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_829')

    def test_css_830(self):
        self.LE.init_runner('test_css_830')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-027.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_829")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_830')

    def test_css_831(self):
        self.LE.init_runner('test_css_831')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-028.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_830")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_831')

    def test_css_832(self):
        self.LE.init_runner('test_css_832')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-029.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_831")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_832')

    def test_css_833(self):
        self.LE.init_runner('test_css_833')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-034.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_832")
        self.LE.test_implicit_expression_screenshot('//*[@id="span1"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="span2"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_833')

    def test_css_834(self):
        self.LE.init_runner('test_css_834')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-035.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_833")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_834')

    def test_css_835(self):
        self.LE.init_runner('test_css_835')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-037.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_834")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_835')

    def test_css_836(self):
        self.LE.init_runner('test_css_836')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-038.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_835")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_836')

    def test_css_837(self):
        self.LE.init_runner('test_css_837')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-039.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_836")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_837')

    def test_css_838(self):
        self.LE.init_runner('test_css_838')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-040.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_837")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_838')

    def test_css_839(self):
        self.LE.init_runner('test_css_839')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-045.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_838")
        self.LE.test_implicit_expression_screenshot('//*[@id="span1"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="span2"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_839')

    def test_css_840(self):
        self.LE.init_runner('test_css_840')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-046.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_839")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_840')

    def test_css_841(self):
        self.LE.init_runner('test_css_841')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-048.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_840")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_841')

    def test_css_842(self):
        self.LE.init_runner('test_css_842')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-049.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_841")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_842')

    def test_css_843(self):
        self.LE.init_runner('test_css_843')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-050.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_842")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_843')

    def test_css_844(self):
        self.LE.init_runner('test_css_844')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-051.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_843")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_844')

    def test_css_845(self):
        self.LE.init_runner('test_css_845')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-056.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_844")
        self.LE.test_implicit_expression_screenshot('//*[@id="span1"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="span2"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_845')

    def test_css_846(self):
        self.LE.init_runner('test_css_846')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-057.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_845")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_846')

    def test_css_847(self):
        self.LE.init_runner('test_css_847')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-058.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_846")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_847')

    def test_css_848(self):
        self.LE.init_runner('test_css_848')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-059.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_847")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_848')

    def test_css_849(self):
        self.LE.init_runner('test_css_849')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-060.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_848")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_849')

    def test_css_850(self):
        self.LE.init_runner('test_css_850')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-061.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_849")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_850')

    def test_css_851(self):
        self.LE.init_runner('test_css_851')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-062.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_850")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_851')

    def test_css_852(self):
        self.LE.init_runner('test_css_852')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-067.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_851")
        self.LE.test_implicit_expression_screenshot('//*[@id="span1"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="span2"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_852')

    def test_css_853(self):
        self.LE.init_runner('test_css_853')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-068.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_852")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_853')

    def test_css_854(self):
        self.LE.init_runner('test_css_854')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-069.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_853")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_854')

    def test_css_855(self):
        self.LE.init_runner('test_css_855')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-070.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_854")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_855')

    def test_css_856(self):
        self.LE.init_runner('test_css_856')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-071.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_855")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_856')

    def test_css_857(self):
        self.LE.init_runner('test_css_857')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-072.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_856")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_857')

    def test_css_858(self):
        self.LE.init_runner('test_css_858')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-073.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_857")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_858')

    def test_css_859(self):
        self.LE.init_runner('test_css_859')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-078.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_858")
        self.LE.test_implicit_expression_screenshot('//*[@id="span1"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="span2"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_859')

    def test_css_860(self):
        self.LE.init_runner('test_css_860')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-079.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_859")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_860')

    def test_css_861(self):
        self.LE.init_runner('test_css_861')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-080.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_860")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_861')

    def test_css_862(self):
        self.LE.init_runner('test_css_862')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-081.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_861")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_862')

    def test_css_863(self):
        self.LE.init_runner('test_css_863')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-082.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_862")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_863')

    def test_css_864(self):
        self.LE.init_runner('test_css_864')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-083.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_863")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_864')

    def test_css_865(self):
        self.LE.init_runner('test_css_865')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-084.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_864")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_865')

    def test_css_866(self):
        self.LE.init_runner('test_css_866')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-089.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_865")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_866')

    def test_css_867(self):
        self.LE.init_runner('test_css_867')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-090.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_866")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_867')

    def test_css_868(self):
        self.LE.init_runner('test_css_868')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-091.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_867")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_868')

    def test_css_869(self):
        self.LE.init_runner('test_css_869')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-095.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_868")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_869')

    def test_css_870(self):
        self.LE.init_runner('test_css_870')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-applies-to-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_869")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_870')

    def test_css_871(self):
        self.LE.init_runner('test_css_871')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-applies-to-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_870")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_871')

    def test_css_872(self):
        self.LE.init_runner('test_css_872')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-applies-to-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_871")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_872')

    def test_css_873(self):
        self.LE.init_runner('test_css_873')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-applies-to-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_872")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_873')

    def test_css_874(self):
        self.LE.init_runner('test_css_874')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-applies-to-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_873")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_874')

    def test_css_875(self):
        self.LE.init_runner('test_css_875')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-applies-to-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_874")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_875')

    def test_css_876(self):
        self.LE.init_runner('test_css_876')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-applies-to-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_875")
        self.LE.test_implicit_expression_screenshot('//*[@id="cell"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_876')

    def test_css_877(self):
        self.LE.init_runner('test_css_877')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-applies-to-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_876")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_877')

    def test_css_878(self):
        self.LE.init_runner('test_css_878')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-applies-to-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_877")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_878')

    def test_css_879(self):
        self.LE.init_runner('test_css_879')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-applies-to-013.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_878")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_879')

    def test_css_880(self):
        self.LE.init_runner('test_css_880')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-applies-to-014.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_879")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_880')

    def test_css_881(self):
        self.LE.init_runner('test_css_881')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-bottom-width-applies-to-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_880")
        self.LE.click_show_test()  # ���show test��ť
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_881')

    def test_css_882(self):
        self.LE.init_runner('test_css_882')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-color-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_881")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_882')

    def test_css_883(self):
        self.LE.init_runner('test_css_883')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-color-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_882")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_883')

    def test_css_884(self):
        self.LE.init_runner('test_css_884')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-color-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_883")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_884')

    def test_css_885(self):
        self.LE.init_runner('test_css_885')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-color-010.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_884")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_885')

    def test_css_886(self):
        self.LE.init_runner('test_css_886')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-color-011.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_885")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_886')

    def test_css_887(self):
        self.LE.init_runner('test_css_887')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-color-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_886")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_887')

    def test_css_888(self):
        self.LE.init_runner('test_css_888')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-color-applies-to-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_887")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_888')

    def test_css_889(self):
        self.LE.init_runner('test_css_889')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-color-applies-to-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_888")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_889')

    def test_css_890(self):
        self.LE.init_runner('test_css_890')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-color-applies-to-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_889")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_890')

    def test_css_891(self):
        self.LE.init_runner('test_css_891')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-color-applies-to-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_890")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_891')

    def test_css_892(self):
        self.LE.init_runner('test_css_892')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-color-applies-to-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_891")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_892')

    def test_css_893(self):
        self.LE.init_runner('test_css_893')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-color-applies-to-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_892")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_893')

    def test_css_894(self):
        self.LE.init_runner('test_css_894')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-color-applies-to-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_893")
        self.LE.test_implicit_expression_screenshot('//*[@id="cell"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_894')

    def test_css_895(self):
        self.LE.init_runner('test_css_895')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-color-applies-to-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_894")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_895')

    def test_css_896(self):
        self.LE.init_runner('test_css_896')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-color-applies-to-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_895")
        self.LE.test_implicit_expression_screenshot('//*[@id="inline-block"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_896')

    def test_css_897(self):
        self.LE.init_runner('test_css_897')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-color-applies-to-013.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_896")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_897')

    def test_css_898(self):
        self.LE.init_runner('test_css_898')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-color-applies-to-014.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_897")
        self.LE.test_implicit_expression_screenshot('//*[@id="table"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_898')

    def test_css_899(self):
        self.LE.init_runner('test_css_899')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-color-applies-to-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_898")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="row"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_899')

    def test_css_900(self):
        self.LE.init_runner('test_css_900')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-color-shorthand-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_899")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_900')

    def test_css_901(self):
        self.LE.init_runner('test_css_901')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-conflict-style-101.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_900")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_901')

    def test_css_902(self):
        self.LE.init_runner('test_css_902')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-conflict-style-102.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_901")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_902')

    def test_css_903(self):
        self.LE.init_runner('test_css_903')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-conflict-style-103.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_902")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_903')

    def test_css_904(self):
        self.LE.init_runner('test_css_904')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-conflict-style-104.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_903")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_904')

    def test_css_905(self):
        self.LE.init_runner('test_css_905')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-conflict-style-105.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_904")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_905')

    def test_css_906(self):
        self.LE.init_runner('test_css_906')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-conflict-style-106.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_905")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_906')

    def test_css_907(self):
        self.LE.init_runner('test_css_907')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-dynamic-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_906")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_907')

    def test_css_908(self):
        self.LE.init_runner('test_css_908')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-dynamic-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_907")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_908')

    def test_css_909(self):
        self.LE.init_runner('test_css_909')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_908")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_909')

    def test_css_910(self):
        self.LE.init_runner('test_css_910')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_909")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_910')

    def test_css_911(self):
        self.LE.init_runner('test_css_911')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_910")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_911')

    def test_css_912(self):
        self.LE.init_runner('test_css_912')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_911")
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_912')

    def test_css_913(self):
        self.LE.init_runner('test_css_913')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-008.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_912")
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_913')

    def test_css_914(self):
        self.LE.init_runner('test_css_914')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-018.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_913")
        self.LE.test_implicit_expression_screenshot('//*[@id="div1"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_914')

    def test_css_915(self):
        self.LE.init_runner('test_css_915')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-applies-to-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_914")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_915')

    def test_css_916(self):
        self.LE.init_runner('test_css_916')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-applies-to-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_915")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_916')

    def test_css_917(self):
        self.LE.init_runner('test_css_917')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-applies-to-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_916")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_917')

    def test_css_918(self):
        self.LE.init_runner('test_css_918')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-applies-to-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_917")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_918')

    def test_css_919(self):
        self.LE.init_runner('test_css_919')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-applies-to-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_918")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_919')

    def test_css_920(self):
        self.LE.init_runner('test_css_920')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-applies-to-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_919")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_920')

    def test_css_921(self):
        self.LE.init_runner('test_css_921')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-applies-to-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_920")
        self.LE.test_implicit_expression_screenshot('//*[@id="cell"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_921')

    def test_css_922(self):
        self.LE.init_runner('test_css_922')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-applies-to-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_921")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_922')

    def test_css_923(self):
        self.LE.init_runner('test_css_923')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-applies-to-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_922")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_923')

    def test_css_924(self):
        self.LE.init_runner('test_css_924')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-applies-to-013.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_923")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_924')

    def test_css_925(self):
        self.LE.init_runner('test_css_925')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-applies-to-014.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_924")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_925')

    def test_css_926(self):
        self.LE.init_runner('test_css_926')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-applies-to-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_925")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="row"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_926')

    def test_css_927(self):
        self.LE.init_runner('test_css_927')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-001.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_926")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_927')

    def test_css_928(self):
        self.LE.init_runner('test_css_928')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-002.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_927")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_928')

    def test_css_929(self):
        self.LE.init_runner('test_css_929')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-003.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_928")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_929')

    def test_css_930(self):
        self.LE.init_runner('test_css_930')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-004.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_929")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_930')

    def test_css_931(self):
        self.LE.init_runner('test_css_931')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-005.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_930")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_931')

    def test_css_932(self):
        self.LE.init_runner('test_css_932')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-006.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_931")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_932')

    def test_css_933(self):
        self.LE.init_runner('test_css_933')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-007.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_932")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_933')

    def test_css_934(self):
        self.LE.init_runner('test_css_934')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-008.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_933")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_934')

    def test_css_935(self):
        self.LE.init_runner('test_css_935')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-009.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_934")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_935')

    def test_css_936(self):
        self.LE.init_runner('test_css_936')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-010.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_935")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_936')

    def test_css_937(self):
        self.LE.init_runner('test_css_937')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-011.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_936")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_937')

    def test_css_938(self):
        self.LE.init_runner('test_css_938')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-012.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_937")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_938')

    def test_css_939(self):
        self.LE.init_runner('test_css_939')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-013.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_938")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_939')

    def test_css_940(self):
        self.LE.init_runner('test_css_940')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-014.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_939")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_940')

    def test_css_941(self):
        self.LE.init_runner('test_css_941')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-015.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_940")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_941')

    def test_css_942(self):
        self.LE.init_runner('test_css_942')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-016.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_941")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_942')

    def test_css_943(self):
        self.LE.init_runner('test_css_943')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-017.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_942")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_943')

    def test_css_944(self):
        self.LE.init_runner('test_css_944')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-018.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_943")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_944')

    def test_css_945(self):
        self.LE.init_runner('test_css_945')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-019.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_944")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_945')

    def test_css_946(self):
        self.LE.init_runner('test_css_946')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-020.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_945")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_946')

    def test_css_947(self):
        self.LE.init_runner('test_css_947')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-021.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_946")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_947')

    def test_css_948(self):
        self.LE.init_runner('test_css_948')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-022.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_947")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_948')

    def test_css_949(self):
        self.LE.init_runner('test_css_949')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-023.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_948")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_949')

    def test_css_950(self):
        self.LE.init_runner('test_css_950')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-024.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_949")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_950')

    def test_css_951(self):
        self.LE.init_runner('test_css_951')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-025.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_950")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_951')

    def test_css_952(self):
        self.LE.init_runner('test_css_952')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-026.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_951")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_952')

    def test_css_953(self):
        self.LE.init_runner('test_css_953')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-027.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_952")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_953')

    def test_css_954(self):
        self.LE.init_runner('test_css_954')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-028.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_953")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_954')

    def test_css_955(self):
        self.LE.init_runner('test_css_955')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-029.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_954")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_955')

    def test_css_956(self):
        self.LE.init_runner('test_css_956')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-030.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_955")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_956')

    def test_css_957(self):
        self.LE.init_runner('test_css_957')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-031.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_956")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_957')

    def test_css_958(self):
        self.LE.init_runner('test_css_958')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-032.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_957")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_958')

    def test_css_959(self):
        self.LE.init_runner('test_css_959')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-033.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_958")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_959')

    def test_css_960(self):
        self.LE.init_runner('test_css_960')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-034.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_959")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_960')

    def test_css_961(self):
        self.LE.init_runner('test_css_961')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-035.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_960")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_961')

    def test_css_962(self):
        self.LE.init_runner('test_css_962')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-036.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_961")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_962')

    def test_css_963(self):
        self.LE.init_runner('test_css_963')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-037.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_962")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_963')

    def test_css_964(self):
        self.LE.init_runner('test_css_964')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-038.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_963")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_964')

    def test_css_965(self):
        self.LE.init_runner('test_css_965')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-039.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_964")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_965')

    def test_css_966(self):
        self.LE.init_runner('test_css_966')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-040.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_965")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_966')

    def test_css_967(self):
        self.LE.init_runner('test_css_967')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-041.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_966")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_967')

    def test_css_968(self):
        self.LE.init_runner('test_css_968')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-042.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_967")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_968')

    def test_css_969(self):
        self.LE.init_runner('test_css_969')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-043.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_968")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_969')

    def test_css_970(self):
        self.LE.init_runner('test_css_970')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-044.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_969")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_970')

    def test_css_971(self):
        self.LE.init_runner('test_css_971')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-045.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_970")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_971')

    def test_css_972(self):
        self.LE.init_runner('test_css_972')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-046.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_971")
        self.LE.test_file_screenshot("test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_972')

    def test_css_973(self):
        self.LE.init_runner('test_css_973')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-047.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_972")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_973')

    def test_css_974(self):
        self.LE.init_runner('test_css_974')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-048.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_973")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_974')

    def test_css_975(self):
        self.LE.init_runner('test_css_975')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-049.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_974")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_975')

    def test_css_976(self):
        self.LE.init_runner('test_css_976')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-050.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_975")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_976')

    def test_css_977(self):
        self.LE.init_runner('test_css_977')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-051.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_976")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_977')

    def test_css_978(self):
        self.LE.init_runner('test_css_978')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-052.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_977")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_978')

    def test_css_979(self):
        self.LE.init_runner('test_css_979')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-053.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_978")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_979')

    def test_css_980(self):
        self.LE.init_runner('test_css_980')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-054.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_979")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_980')

    def test_css_981(self):
        self.LE.init_runner('test_css_981')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-055.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_980")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_981')

    def test_css_982(self):
        self.LE.init_runner('test_css_982')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-056.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_981")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_982')

    def test_css_983(self):
        self.LE.init_runner('test_css_983')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-057.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_982")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_983')

    def test_css_984(self):
        self.LE.init_runner('test_css_984')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-058.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_983")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_984')

    def test_css_985(self):
        self.LE.init_runner('test_css_985')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-059.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_984")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_985')

    def test_css_986(self):
        self.LE.init_runner('test_css_986')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-060.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_985")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_986')

    def test_css_987(self):
        self.LE.init_runner('test_css_987')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-061.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_986")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_987')

    def test_css_988(self):
        self.LE.init_runner('test_css_988')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-062.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_987")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_988')

    def test_css_989(self):
        self.LE.init_runner('test_css_989')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-063.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_988")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_989')

    def test_css_990(self):
        self.LE.init_runner('test_css_990')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-064.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_989")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_990')

    def test_css_991(self):
        self.LE.init_runner('test_css_991')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-065.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_990")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_991')

    def test_css_992(self):
        self.LE.init_runner('test_css_992')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-066.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_991")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_992')

    def test_css_993(self):
        self.LE.init_runner('test_css_993')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-067.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_992")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_993')

    def test_css_994(self):
        self.LE.init_runner('test_css_994')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-068.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_993")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_994')

    def test_css_995(self):
        self.LE.init_runner('test_css_995')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-069.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_994")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_995')

    def test_css_996(self):
        self.LE.init_runner('test_css_996')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-070.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_995")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_996')

    def test_css_997(self):
        self.LE.init_runner('test_css_997')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-071.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_996")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_997')

    def test_css_998(self):
        self.LE.init_runner('test_css_998')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-072.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_997")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_998')

    def test_css_999(self):
        self.LE.init_runner('test_css_999')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-073.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_998")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_999')

    def test_css_1000(self):
        self.LE.init_runner('test_css_1000')  # ��runnerҳ��
        self.LE.remove_checkbox()
        self.LE.send_path('css/CSS2/borders/border-left-color-074.xht')  # �Ƿ����ָ��·�� Ĭ����/ ��ȫ��·��
        self.LE.start_show_test("css_999")
        self.LE.test_implicit_expression_screenshot('//*[@id="test"]', "test")  # testҳ���ͼ
        self.LE.test_implicit_expression_screenshot('//*[@id="reference"]', "test")  # testҳ���ͼ
        self.LE.click_show_ref()  # ���show reference��ť
        self.LE.ref_file_screenshot("ref")  # referenceҳ���ͼ
        self.LE.test_assert("test", "ref")  # ����
        self.LE.runner_end('test_css_1000')