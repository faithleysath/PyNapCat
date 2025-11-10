"""
Python 3.14 类型安全特性演示

本示例展示了 PyNapCat 如何利用 Python 3.14 的延迟注解求值（PEP 649/749）
实现 TypeScript 级别的类型安全。
"""

from annotationlib import get_annotations, Format
from typing import Protocol, TypeVar


# ============================================
# 1. 前向引用无需字符串包裹
# ============================================

class Node:
    """在 Python 3.14 中，前向引用自动处理，无需手动包裹为字符串"""
    value: int
    next: Node | None  # 在 3.13 及之前需要写成 'Node | None'
    
    def __init__(self, value: int, next: Node | None = None):
        self.value = value
        self.next = next


# ============================================
# 2. 使用 annotationlib 安全读取注解
# ============================================

def inspect_annotations_safely():
    """演示如何安全地读取和处理注解"""
    
    # VALUE 格式：完全求值（可能触发 NameError）
    try:
        annotations_value = get_annotations(Node, format=Format.VALUE)
        print("VALUE 格式（完全求值）:")
        print(f"  {annotations_value}")
    except NameError as e:
        print(f"VALUE 格式失败: {e}")
    
    # FORWARDREF 格式：未定义的名用 ForwardRef 包裹
    annotations_forwardref = get_annotations(Node, format=Format.FORWARDREF)
    print("\nFORWARDREF 格式（安全）:")
    for name, annotation in annotations_forwardref.items():
        print(f"  {name}: {annotation}")
    
    # STRING 格式：返回字符串表示
    annotations_string = get_annotations(Node, format=Format.STRING)
    print("\nSTRING 格式（字符串表示）:")
    for name, annotation in annotations_string.items():
        print(f"  {name}: {annotation}")


# ============================================
# 3. 泛型类型的现代语法
# ============================================

T = TypeVar('T')

class Stack[T]:  # Python 3.12+ 的泛型语法
    """类型安全的栈实现"""
    
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def push(self, item: T) -> None:
        """压入元素"""
        self._items.append(item)
    
    def pop(self) -> T:
        """弹出元素"""
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()
    
    def peek(self) -> T | None:
        """查看栈顶元素"""
        return self._items[-1] if self._items else None


# ============================================
# 4. 协议（Protocol）与结构化类型
# ============================================

class Drawable(Protocol):
    """可绘制对象的协议"""
    
    def draw(self) -> str:
        """绘制对象"""
        ...


class Circle:
    """圆形 - 实现了 Drawable 协议"""
    
    def __init__(self, radius: float):
        self.radius = radius
    
    def draw(self) -> str:
        return f"Circle(radius={self.radius})"


class Rectangle:
    """矩形 - 实现了 Drawable 协议"""
    
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def draw(self) -> str:
        return f"Rectangle({self.width}x{self.height})"


def render(shape: Drawable) -> None:
    """渲染任何可绘制对象"""
    print(f"Rendering: {shape.draw()}")


# ============================================
# 5. 异步类型注解
# ============================================

from typing import Awaitable, Callable
from collections.abc import AsyncIterator


async def async_process[T](
    items: AsyncIterator[T],
    processor: Callable[[T], Awaitable[T]]
) -> list[T]:
    """异步处理迭代器中的所有项目"""
    results: list[T] = []
    async for item in items:
        processed = await processor(item)
        results.append(processed)
    return results


# ============================================
# 主演示函数
# ============================================

def main():
    """运行所有演示"""
    print("=" * 60)
    print("Python 3.14 类型安全特性演示")
    print("=" * 60)
    
    # 1. 前向引用演示
    print("\n[1] 前向引用:")
    node1 = Node(1)
    node2 = Node(2, node1)
    print(f"  创建链表节点: {node2.value} -> {node2.next.value if node2.next else None}")
    
    # 2. 注解读取演示
    print("\n[2] 安全的注解读取:")
    inspect_annotations_safely()
    
    # 3. 泛型演示
    print("\n[3] 泛型类型安全:")
    int_stack: Stack[int] = Stack()
    int_stack.push(1)
    int_stack.push(2)
    print(f"  栈顶元素: {int_stack.peek()}")
    
    str_stack: Stack[str] = Stack()
    str_stack.push("hello")
    str_stack.push("world")
    print(f"  字符串栈: {str_stack.peek()}")
    
    # 4. 协议演示
    print("\n[4] 结构化类型（Protocol）:")
    circle = Circle(5.0)
    rectangle = Rectangle(10.0, 20.0)
    render(circle)
    render(rectangle)
    
    print("\n" + "=" * 60)
    print("所有演示完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
