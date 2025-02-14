import os
import json
import tempfile
import shutil
import unittest
from china_stock_data.persistent_dict import PersistentDict

class TestPersistentDict(unittest.TestCase):
    def setUp(self):
        # 创建临时目录用于测试
        self.test_dir = tempfile.mkdtemp()
        test_data_dir = os.path.join(self.test_dir, 'test_data')
        os.makedirs(test_data_dir, exist_ok=True)
        self.test_file = os.path.join(test_data_dir, 'test_dict.json')
        self.test_dict = PersistentDict(self.test_file)

    def tearDown(self):
        # 清理临时目录
        shutil.rmtree(self.test_dir)

    def test_init_creates_directory(self):
        """测试初始化时是否正确创建目录"""
        self.assertTrue(os.path.exists(os.path.dirname(self.test_file)))

    def test_set_and_get(self):
        """测试设置和获取值"""
        self.test_dict.set('key1', 'value1')
        self.assertEqual(self.test_dict.get('key1'), 'value1')
        
        # 测试默认值
        self.assertEqual(self.test_dict.get('non_existent', 'default'), 'default')

    def test_delete(self):
        """测试删除键值对"""
        self.test_dict.set('key2', 'value2')
        self.test_dict.delete('key2')
        self.assertIsNone(self.test_dict.get('key2'))

    def test_get_all(self):
        """测试获取所有数据"""
        test_data = {'key3': 'value3', 'key4': 'value4'}
        for k, v in test_data.items():
            self.test_dict.set(k, v)
        
        self.assertEqual(self.test_dict.get_all(), test_data)

    def test_persistence(self):
        """测试数据持久化"""
        # 写入数据
        self.test_dict.set('key5', 'value5')
        
        # 创建新的实例读取数据
        new_dict = PersistentDict(self.test_file)
        self.assertEqual(new_dict.get('key5'), 'value5')

    def test_file_content(self):
        """测试文件内容格式"""
        test_data = {'key6': 'value6'}
        self.test_dict.set('key6', 'value6')
        
        with open(self.test_file, 'r') as f:
            file_content = json.load(f)
        
        self.assertEqual(file_content, test_data)

    def test_complex_data_types(self):
        """测试复杂数据类型的存储"""
        complex_data = {
            'list': [1, 2, 3],
            'dict': {'a': 1, 'b': 2},
            'nested': {'x': [1, 2, {'y': 3}]}
        }
        self.test_dict.set('complex', complex_data)
        self.assertEqual(self.test_dict.get('complex'), complex_data)

    def test_has(self):
        """测试键值存在性检查"""
        self.test_dict.set('test_key', 'test_value')
        
        # 测试存在的键
        self.assertTrue(self.test_dict.has('test_key'))
        
        # 测试不存在的键
        self.assertFalse(self.test_dict.has('non_existent_key'))

if __name__ == '__main__':
    unittest.main()
