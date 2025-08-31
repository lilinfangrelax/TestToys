# 测试用例管理模块

## 导入

从其他系统导出的数据，可导入到本工具（TestToys）中。

实现方法
1. TestToys的数据库“测试用例”表字段是固定的
2. 从其他数据库中导出的数据，只需要在导入时映射到对应字段上，多余字段则可以放置在单独一列（需要时就进行解析）

### “测试用例”表字段

- 用例名称
- 用例编号
- 等级
- 前提条件
- 测试步骤
- 预期结果
- 备注
- 用例标签
- 修改时间
- 创建时间
- 扩展字段1
- 扩展字段2
- 扩展字段3
- 扩展字段4
- 扩展字段5
- 其他字段



---



# Test Case Management Module

## Import

Data exported from other systems can be imported into this tool (TestToys).

Implementation Method
1. The fields in TestToys' “Test Cases” database table are fixed.
2. When importing data from other databases, simply map the fields to their corresponding counterparts. Any extra fields can be placed in a separate column (to be parsed as needed).

### “Test Cases” Table Fields

- Test Case Name
- Test Case ID
- Level
- Prerequisites
- Test Steps
- Expected Results
- Notes
- Test Case Tags
- Modified Time
- Created Time
- Extended Field 1
- Extended Field 2
- Extended Field 3
- Extended Field 4
- Extended Field 5
- Other Fields