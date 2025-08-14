import subprocess
import pytest

if __name__ == '__main__':
    # 运行 pytest，显示详细信息和日志
    pytest.main(['-v', '--log-cli-level=INFO'])

    # 生成 allure 报告
    subprocess.run("allure generate temp -o report --clean", shell=True, check=True)
    print("Allure report generated at ./report")
