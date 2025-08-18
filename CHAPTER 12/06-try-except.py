def demo(choice):
    try:
        if(choice == 1):
            result = 10/0
        elif(choice==2):
            result = "5"+2
        elif(choice==3):
            nums = [1,2,3]
            result = nums[10]
        else:
            print("No error here 🚀")
            return
    except ZeroDivisionError:
        print("❌ Oops! Division by zero is not allowed.")
    except TypeError:
        print("❌ Type mismatch! You tried mixing incompatible types.")
    except Exception as e:   # safer than bare except
        print(f"⚠️ Some other error occurred: {e}")

demo(2)


# #usinng else
# def demo(choice):
#     try:
#         if choice == 1:
#             print("Dividing by zero...")
#             result = 10 / 0
#         else:
#             print("Doing safe math...")
#             result = 10 / 2
#     except:
#         print("❌ An error occurred!")
#     else:
#         print("✅ Success! The result is:", result)

# # Test
# demo(1)  # error
# print("---")
# demo(2)  # no error




#using finally

# def demo(choice):
#     try:
#         if choice == 1:
#             print("Dividing by zero...")
#             result = 10 / 0
#         else:
#             print("No error here 🚀")
#     except:
#         print("❌ An error occurred!")
#     finally:
#         print("🔚 This always runs (cleanup, closing files, etc.)")

# # Test
# demo(1)  # Exception case
# print("---")
# demo(2)  # No exception
