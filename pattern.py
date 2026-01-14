n =5

# *
# *
# *
# *
# *

# for i in range(n):
#     print("*")



#* * * * * 

# for i in range(n):
#     print("*",end=" ")



# * * * * * 
# * * * * * 
# * * * * *
# * * * * *
# * * * * *

# for i in range(n):
#     print("* "*n)



# * 
# * * 
# * * *
# * * * *
# * * * * *

# for i in range(n):
#     for j in range(i+1):
#         print("* ",end="")
#     print("")




# * * * * * 
# * * * * 
# * * *
# * *
# *

# for i in range(n):
#     for j in range(n-i):
#         print("* ", end="")
#     print("")



#         * 
#       * *
#     * * *
#   * * * *
# * * * * *

# for i in range(n+1):
#     space = 2*(n-i)
#     star = i
#     print(space * (" ") + star * ("* "))



# * * * * * 
#   * * * * 
#     * * *
#       * *
#         *

# for i in range(n):
#     space = 2 * i
#     star = n-i
#     print(space * (" ") + star * ("* "))



#     * 
#    * *
#   * * *
#  * * * *
# * * * * *

# for i in range(n+1):
#     space = n-i
#     star = i
#     print(space * (" ") + star * ("* "))





#    * 
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# for i in range(n):
#     space = n-i
#     star = i
#     print(space * (" ") + star * ("* "))
# for j in range(i+1):
#     space = j
#     star = n-j
#     print(space * (" ") + star * ("* "))



# *                 * 
# * *             * * 
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *

# for i in range(1,n+1):
#     space = 4*(n-i)
#     star = i
#     print(star * ("* ") + space * (" ") + star * ("* "))




# * * * * * 
# *       * 
# *       * 
# *       * 
# * * * * *
# for i in range(1,n+1):
#     if i == 1 or i == n:
#         print("* " * n)
#     else:
#         space = 2*(n-2)
#         print("* " + space * (" ") + "* ")



#     *
#    * *
#   *   *
#  *     *
# * * * * *

# for i in range(1,n+1):
#     if i==1:
#         space = n-1
#         print(space * (" ") + "*")
#     elif i==n:
#         print("* " * n)
#     else:
#         space1 = n - i
#         space2 = 2*(i-2)+1
#         print(space1 * (" ") + "*" + space2 * (" ") + "*")






# * 
# * * 
# *   * 
# *     * 
# * * * * * 

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==1 or j==i or i==n:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print("")





#         *
#       * *
#     *   *
#   *     *
# * * * * *

# for i in range(1, n+1):
#     if i == 1:
#         space = (n-1) *2 
#         print(space * (" ") + "*")
#     elif i == n:
#         print("* " * n)
#     else:
#         space1 = 2*(n - i)
#         space2 = 2*(i-2)+1
#         print(space1 * (" ") + "*" + space2 * (" ") + "*")