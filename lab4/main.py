from stack import Stack
from myQueue import Queue
from matrix import Matrix

stack = Stack([])
print(stack.get_stack())
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.get_stack())
print(stack.pop(), stack.pop(), stack.pop(), stack.pop())
stack.push(5)
print(stack.peek(), stack.pop(), stack.peek())
stack.push(6)
print(stack.get_stack())


q = Queue([])
q.push(2)
q.push(3)
q.push(4)
print(q.pop())
print(q.peek())
print(q.get_queue())


matrix = Matrix(2, 3)
matrix.set(1, 1, 5)
matrix.set(1, 0, 6)
print(matrix.matrix)

# matrix.transpose()
#
# print(matrix.matrix)
# print(matrix.rows)
# print(matrix.cols)


matrix2 = Matrix(3, 2)

matrix2.set(1, 1, 5)
matrix2.set(0,0, 6)

print(matrix.multiply(matrix2).matrix)

matrix.apply(lambda x: x * 2)
print(matrix.matrix)
