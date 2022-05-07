#comment all functions

"""Importing tkinter and setting up our window"""

from tkinter import *

window = Tk()
window.title("Rejection Letter Builder - TY, FU, Bye!")
window.configure(background="lightblue")

text_standard = "\n\nthank you for your application. Unfortunately we cannot offer you a job."
text_formal = "\n\nUnfortunately, our team did not select you for further consideration.  I would like to note that competition for jobs at our company name is always strong and that we often have to make difficult choices between many high-caliber candidates. Now that we’ve had the chance to know more about you, we will be keeping your resume on file for future openings that better fit your profile.  I am happy to answer your questions if you would like any specific feedback about your application or interviews."
text_sweet = "\n\nWe ended up moving forward with another candidate, but we’d like to thank you for talking to our team and giving us the opportunity to learn about your skills and accomplishments.  We will be advertising more positions in the coming months. We hope you’ll keep us in mind and we encourage you to apply again.  We wish you good luck with your job search and professional future endeavors."
text_constructive = "\n\nI want to thank you for your interest in and for all of the time you have put into the application. Unfortunately, we will not be offering the position to you. While your education qualifications are very impressive, we have chosen a candidate who has more hands-on experience. We will keep your resume on file, and if any other job positions become available we will keep you in mind."
reapply_text = "\n\nPlease don't be disappointed. Feel free, to reapply!\n"
dont_reapply_text = ""


"""
Creating an empty textbox on the right side
"""
rejection_text_box = Text(window, width=60, height=40, borderwidth=3)
rejection_text_box.grid(row=0, column=2, rowspan=20)


"""
Creating labels and empty Entry() boxes: 
Applicant's name company name, job position etc.
Note: we are using Entry() and not Text() as a widget!
Entry() allows only one single line and the height is always 1.
Text() allows multiple lines of String.
"""

#Applicant Name
instruction_give_candidate_name = Label(window, text="Enter applicant's \n name below:")
instruction_give_candidate_name.grid(row=0, column=0)
candidate_name_text_box = Entry(window, width=40, borderwidth=3)
candidate_name_text_box.grid(row=1, column=0) 

#Job Title
instruction_give_job_title = Label(window, text="Enter job title \n below:")
instruction_give_job_title.grid(row=4, column=0)
job_title_text_box = Entry(window, width=40, borderwidth=3)
job_title_text_box.grid(row=5, column=0)

#Company Name
instruction_give_company_name = Label(window, text="Enter company's \n name below:")
instruction_give_company_name.grid(row=8, column=0)
company_name_text_box = Entry(window, width=40, borderwidth=3)
company_name_text_box.grid(row=9, column=0) 

#Sender Name
instruction_give_name_sender = Label(window, text="Enter sender name \n below:")
instruction_give_name_sender.grid(row=12, column=0)
give_name_sender_text_box = Entry(window, width=40, borderwidth=3)
give_name_sender_text_box.grid(row=13, column=0)

#Text Style Listbox Format
instruction_choose_text_style = Label(window, text="Adapt the letter's style:")
instruction_choose_text_style.grid(row=16, column=0)
choose_text_style_box = Listbox(window)
choose_text_style_box.config(width=0,height=0)

#Inserting Text Styles
choose_text_style_box.grid(row=17, column=0)
choose_text_style_box.insert(1,'Formal')
choose_text_style_box.insert(2,'Sweet')
choose_text_style_box.insert(3,'Constructive')
choose_text_style_box.grid(row=17, column=0)


def give_greeting():
    #returns String: Greeting + Name
    get_name = candidate_name_text_box.get()
    personal_greeting = "Dear " + get_name +","
    print(personal_greeting)
    return(personal_greeting)

def give_job_and_company():
    #returns String: Thanks + Company + Position
    get_job = job_title_text_box.get()
    get_company = company_name_text_box.get()
    job_and_company = "\n\nthank you for applying for the " +get_job +" position at "+get_company+"."
    print(job_and_company)
    return(job_and_company)

def give_selected_text_style():
    #returns the String value from listbox selection
    selection = choose_text_style_box.get(choose_text_style_box.curselection())
    if selection == 'Formal':
        return (text_formal)
    elif selection == 'Sweet':
        return (text_sweet)
    elif selection == 'Constructive':
        return(text_constructive)
    else:
        print("no text style selected.")
        return (text_standard)
   
def reapply_button_check():
    #returns a String if Button is checked
    if reapply_boolean.get():
        print("reapply checked")
        return (reapply_text)
    else:
        print("reapply button not checked")
        return(dont_reapply_text)

def give_sender():
    #returns a farewell formula as String + Sender name
    goodbye_sender = "\n\nSincerly\n\n" + give_name_sender_text_box.get()
    return(goodbye_sender)

#Inserting a Re-Apply Checkbutton
reapply_boolean=IntVar()
Checkbutton(window, text = "Ask to Reapply", variable=reapply_boolean, onvalue=1, 
            offvalue=0, command=reapply_button_check).grid(row=18, column=0)



#Generate Text Button
'''
Configurung what the Generate Text button does
1.  the press_generate_text_button function must come first
2.  in the rejection_textbox is a Text()-widget not an Entry()-widget:
    Text widgets allow multiple lines of strings
    Entry widgets only allow one string line (e.g. for a calculator)
    So to delete/insert a string 
    in the range of 0 and end of file
    it is important to use doubles needed for 'Text' (0.0 respectively 1.0 etc.) 
    and NOT Integers needed for 'Entry' (0 respectively 1 etc.) 
'''
def press_generate_text_button():
    rejection_text_box.delete(0.0, "end")
    rejection_text_box.insert(END, give_greeting())
    rejection_text_box.insert(END, give_job_and_company())
    rejection_text_box.insert(END, give_selected_text_style())
    rejection_text_box.insert(END, reapply_button_check())
    rejection_text_box.insert(END, give_sender())


text_generator_button = Button(window, text = "PRESS TO GENERATE \nYOUR TEXT", 
    command = lambda: 
        [
            press_generate_text_button(),            
            reapply_button_check(),
            give_selected_text_style(),
            print(give_selected_text_style())
         ])
text_generator_button.grid(row=33, column=0)





window.mainloop()