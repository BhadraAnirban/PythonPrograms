| Package/Method        | Description |
|----------------------|------------|
| **Packaging** | To create a package, the folder structure is as follows: <br> Project folder → Package name → `__init__.py`, `module_1.py`, `module_2.py`, etc. <br> In `__init__.py`, add code to reference modules. |
| **Python Style Guide** | Follow coding standards: <br> • Use 4 spaces for indentation <br> • Use blank lines between functions/classes <br> • Add spaces around operators and commas <br> • Write logic inside functions <br> • Use `lowercase_with_underscores` for functions/files <br> • Use `CamelCase` for classes <br> • Use `UPPER_CASE` for constants |
| **Static Code Analysis** | Evaluate code quality without execution using tools like **Pylint**. |
| **Unit Testing** | Unit testing validates code behavior. Each unit is tested independently, often in CI/CD pipelines, using assertions to verify correctness. |

---

## 📦 Packaging Example

```python
# module1.py
def function_1(arg):
    return arg * 2   # example operation