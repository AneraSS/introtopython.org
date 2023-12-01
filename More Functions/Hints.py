def thank_you(name='everyone'):
    # This function prints a two-line personalized thank you message.
    #  If no name is passed in, it prints a general thank you message
    #  to everyone.
    print("\nYou are doing good work, %s!" % name)
    print("Thank you very much for your efforts on this project.")


thank_you('Adriana')
thank_you('Billy')
thank_you('Caroline')
thank_you()

