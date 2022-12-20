                                                This is a online gym app

                                                        Feature:
                                       . Has an admin management side and customer side.
                                       . Signup to be one of the gym member.
                                       . To check in if you are already a member.
                                       . Could delete and edit classes as a admin.
                                       . Could check members check in status.
                                       . Could know what classes will hold today.
                                       . Could check out all the members datails.
                                       . Classes would change regarding the what weekday the current day is.

                                                        How:
                                         I created three tables inside the database,
                                             . Members
                                             . Classes
                                             . Classes_attend (This table store the member's id
                                               and class id when a member join a class.)

                                         Members table will be updated whenever a customer
                                       decided to join the gym(Signup).

                                         Customers need to check in on the website before   
                                       they enter the gym.(Once they checked in the check-in
                                       value would be True and admin could track whoever checked-
                                       in.)

                                         Data from the classes_attend table will be showed in the
                                       admin's home page to show who should be showing up today.

                                                        Future Feature:
                                       . Log in function
                                       . Members able to check the profile along with the attendence
                                       . Members could choose which plan to subscribe and each has
                                         different privilege.



