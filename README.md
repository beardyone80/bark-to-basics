# Welcome to Bark to Basics

Bark to basics is the go to site for your introduction to dog care. If you are considering getting a dog, are a new owner or are just having trouble caring for your dog, Bark to Basics has just what you need.

This site was constructed over three days during a hackathon by the aptly named Hackathon team 1. The team consisted of Paul (Team lead), Hibo, Stacey, Rachel, and Charles.

## Day 1

The majority of the first day was spent doing ideation, sorting out user stories, and creating wireframes. We were originally going to create a learning management system, but after some advice from tutors and mentors, we decided to simplify the site into a few lessons.

We decided to do an informative site about animals, as one of our team members had a background in zoology. This was narrowed down to a dog training site as there were a number of things that could be used for potential lessons.

From there, the user stories were written:

1.  As a potential dog owner I want to get information about how to best look after a dog so that I can be a better dog owner.

2.  As a dog owner I want to make sure I'm caring for my dog correctly so that I can make sure my dog is happy.

3.  As an admin I want to receive feedback on the learning material so I can improve the site.

4.  As a user I want to leave feedback if I'm unsure about the content so that the content can be improved by the site owner.

5.  As a dog owner I want to test my knowledge regarding caring for dogs so that I can feel more confident as a dog owner.

6.  As a pet owner I want to get answers to specific questions regarding my dog so that I can solve problems I am facing with my dog.

7.  As a pet owner I want to create a user account so that I can view additional information.

These user stories were then converted into issues and placed into our project board which can be viewed at <https://github.com/users/beardyone80/projects/5>

Then, Paul created wireframes using the Balsamiq wireframe creation tool.

### Home page

![](https://lh7-us.googleusercontent.com/sQM3zpKbpvf7iRcF25z3Psj_3C79H-0jHvRjprnNzXtLHrS-Lqi8S_QKqkUvQThyTpejijejFezP8Qx8o7-GkFgRlMxjOW7KATPVTdOehz6Obi0Tix24jnnaoer6swTNXyzr0NbM-LRHqMn8IxlvHfs)

### Logged-in page

![](https://lh7-us.googleusercontent.com/vBnQJegcHfCMN7dLSwUt_X15QqMPCFuWPJgH-YUIpJLRon6zLWG8LRKAoW4QU1CRxh8xqu1ZwqRE7YHgKlj7kDucZNxGpV01ritUF1HsExvnii3kfpBuQYor4nIkbOnHJZvcLiN5-AKW0PiAYv40uC0)

### Detailed post page

![](https://lh7-us.googleusercontent.com/3z9u6GrMDaBi3_diVLYDTlYr7FC9jiyKyYvQgRcA4W-2Ue-hK2ZeK0-rKWVlyZ9C1RENNtr-5Y8h5zUTusw9soY9VJJJvyA8IT2hw89PAS1Sq5iHGjmLFj3ofPW64D4lyUP60sc3qtHm652UvtENhng)

### Quiz page

![](https://lh7-us.googleusercontent.com/CPq0LiEA_vHOIjAniZaUxtN6KxaFSAyA1s2OFkvc9pJphHvLNWYtXjj8PJeTFT0DJHiaCOY-zBX-c37u14102NApgUjDuR6IDRjXQXFon_EURnJPC-iYaXypku02pZqlW58M9xiIJKBgeT0f0Y8FxHE)

It was decided that the quiz was out of scope for this project, but the other pages could be made within the three days.

In the afternoon, we started coding. It was agreed that, to start, it would be best for one person to set up django and create the first apps. The person coding would share their screen and the others would check for mistakes as they went, as well as aid in the general construction of the files.

## Day 2

The second day involved more coding together. The my_project, home and lesson apps were all constructed, and so we got to constructing the models, views and templates.

### Basic home page with header and footer (no info)

![](https://lh7-us.googleusercontent.com/6W2VJY_z2F4KHY2Us-YEsFURgF2Q4RslcpaSPTi_wfZ6wV-v-Q0135rNSu9xqtc4X-oIQ9mxX1xR04tfC_VkooFNwwERVXxyKh8c5WBFl49ejZ6j4vdBHOJMdMWszH575DzY4OykIpOJ7C7-fWCNqhs)

### Add lesson page (top)

![](https://lh7-us.googleusercontent.com/Ko1HgMmxSU0Q9kLXj1-uhMYccDlqGX3jCWbeuo_hvs44lO1A-tDZI0Ye8HgIMQWA2U_DMI1K71Wp0Jp_CHeimLvk0CrDAfCCHxWKrZmOVqtCJhJh72dLTi9DZnV63zQrS7QqhilJMzN_MemS8lCZqpA)

### Add lesson (bottom)

![](https://lh7-us.googleusercontent.com/Qe_s2mvSI-LLuWZx2cQHTZKUmcZBfuJPWtkdOYcIOmtiTE8eKwJDj2-mCr2FBLp3vH899kCqBDZot0jXrAjohESm6Eya9JHpMDKLMJaVaMAS2xiPiuinWDX8vDh7ocaJUb1zClqdX2qrjc6-kqpAS9c)

We installed Django-allauth and used their basic pages to create register, login, and sign out pages. (Register and sign out had no styling at this point)

### Login page

![](https://lh7-us.googleusercontent.com/raasdRhslejjA40e_Jmcc4-L8idAwURDeQbEibH3OM018N-1fH8SAP0td2K09LeUA6leITqJ01kG4Vf0fCy_fuGoJLXREa9-nMl-hUe8TRb_6N1hGdSCe6MHlTBKVgqK7INFvwuTmmLZXWbiqi3XC5Q)

We encountered a few errors along the way, but these were usually caused by format errors or problems with installed content. We had to consult the tutors for one particular error which we could not fix, it turned out it was due to incorrect variables being returned in one of our models.

## Day 3

On the third day, we cracked on with coding. Hibo was put on to styling, Rachel was in charge of implementing the detail and comments pages, Paul was in charge of the home page, and Charles was updating the README. 

Progress was made quickly, as the majority of the tedium involved with setting up django had finished.

### New home page

![](https://lh7-us.googleusercontent.com/xEv1PZGh2eLMQBglFudgUAFbypobmw5RhgHZbeV5dY2I78y25wWp1vhAvDsdla0faDZ0j-n-okZn40nQnDVwZwk7kFSGGjDxP0hb7TwlLEg8a3cPYk6gJgOm_ccf2DXZO-A-HwQvwLXc_oJNyc-kOWQ)

### Sign up page with styling

![](https://lh7-us.googleusercontent.com/7LStwjeiOdxr82XjLTUc86LLDfw3sFUYIpgfYgMpAc-jm_M27fJlg4SwmPqU4NT3WWndZ7Xv2-qEr-l9bfBbW2fWUG5mtRbfSVzfLWDvSIsHLHi8OG7ZhMtZ9YPjfqEZ__smP7JX-KcLzPN0JxOzTYI)

### Detail page (example)

![](https://lh7-us.googleusercontent.com/zCCVYoB6LTJTm9EpJ1q-rbN4PPW77FasEahFNUilf2S6x9e0mpAEkx5NVQIasH_3PZF6xNrJpqEs3FK7FQqR4Yk-PO3XD6HI58a3kjIqbCr0lpcPdCouVnrhQO8FBBgpjkJcUWXfd_z9RKRyAnKckWk)

### Media used

Images: 

-   Hero image from <https://www.pexels.com/>

Content:

-   The icons throughout the page were taken from [Font Awesome](https://fontawesome.com/)

-   Instructions and code for using Bootstrap was used and edited from that which can be found on the official [BootStrap Site](https://getbootstrap.com/)

ChatGPT was used to identify bug fixes
