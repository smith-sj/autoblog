# Autoblog

## About

I wrote this Python script while working on a static HTML site for my first bootcamp assignment. One of the requirements for this assignment
was to include multiple blog posts and, as I soon discovered, the process of updating a blog on a static website is extremely tedious. Thanks
to the way my site was set up, these are the steps I had to go through when writing a new post:

1. Open up blog post template, fill in new post, save with title numbered correctly
2. Add a link in new blog post to previous blog post
3. Open up previous blog post and add link to new blog post
4. Open up blog archive and add a new link to the new blog post
    * Add date
    * Add category tags 
6. Open up homepage and edit the 'Recent Posts' section:
    * Add new post to top of 'Recent Posts' list
        * Add date
        * Add category tags 
    * Remove oldest post from the "Recent Posts" list

Someone who wasn't bored and stuck in COVID isolation would say *"It's okay, it's just an assignment, I can deal with it for now and it won't even matter
when we finally learn static site generators and frameworks."* Obviously, that's not what I said. Instead I decided to use the little Python knowledge I have to automate the task.

Now with the program complete, my blog posting process looks like this:

1. Write blog post in the postcontent.txt file
2. Run Autoblog and answer the prompts

That's it!

## Built With

Python (jinja2, BeautifulSoup)

HTML

## How It Works

I commented almost every line as I'll probably forget how it works, but it also makes it an easy read for anyone who wants to have a peak. It's also important 
to point out that, while I've set some of the variables as inputs, a lot of the script is specific to my portfolio. If I get some free time during 
the bootcamp, I'd like to come back and abstract certain parts so it can be used for various projects.

Here's a quick overview of how it works:

1. The user types their blog post (including HTML tags) into postcontent.txt
2. On initial running of Autoblog, the user is prompted for some inputs:
    * ***post number***
    * ***post title***
    * ***post categories***
    * ***post date***
4. Autoblog checks the blog directory to make sure the user has entered the right ***post number***
    * If the ***post number*** already exists or if the user has skipped a number, then Autoblog corrects it
6. Autoblog then opens up the blog post template and parses the HTML
7. Using content from *postcontent.txt* and input data from the user, Autoblog populates the blog template appropriately
8. The post is saved to the blog post directory with correctly numbered title
9. The user is asked if they'd like to add a link to previous post
    * an incorrect input to any yes or no question will trigger Autoblog to ask again
10. If yes, Autoblog opens the previous blog post and adds a link to the new post
11. The user is asked if they'd like to add post to Archive
12. If yes, Autoblog opens the blog archive and adds a styled blog link with appropriate date and categories
    * Autoblog removes commas from ***post categories*** and adds them as classes to the HTML element
13. The user is asked if they'd like to add post to Recent Posts (a section on my homepage)
14. If yes, Autoblog opens the homepage and adds a styled blog link with appropriate date and categories
15. Autoblog also removes the oldest post from the Recent Post list

And that's pretty much it.

## To Do:

1. Some refactoring and abstraction: make it usable for various projects
2. Play around with the html parser: try and get it to format the exact way I like it

