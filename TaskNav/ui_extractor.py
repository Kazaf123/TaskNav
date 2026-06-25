import xml.etree.ElementTree as ET
import json


class UIExtractor:
    def __init__(self, ocr_engine="tesseract"):
        self.ocr_engine = ocr_engine

    def parse_view_tree(self, xml_path):
        """解析 Android UIAutomator 导出的 XML 视图树"""
        tree = ET.parse(xml_path)
        root = tree.getroot()
        components = []

        for idx, node in enumerate(root.iter('node')):
            bounds = node.attrib.get('bounds', '[0,0][0,0]')
            text = node.attrib.get('text', '')
            content_desc = node.attrib.get('content-desc', '')
            class_type = node.attrib.get('class', '')

            # 过滤掉既没有文本也没有内容的纯布局节点
            if not text and not content_desc and class_type.endswith('Layout'):
                continue

            component = {
                "id": idx,
                "text": text or content_desc,
                "type": class_type.split('.')[-1],
                "bounds": bounds,
                "hierarchy": "Root > " + class_type.split('.')[-1]  # 简化表示
            }
            components.append(component)
        return components

    def extract_multimodal_representation(self, xml_path, screenshot_path):
        """融合结构树与视觉特征 (此处视觉特征简化为占位)"""
        # 实际应用中可在此处调用 OCR 和目标检测识别 Icon
        components = self.parse_view_tree(xml_path)
        return components