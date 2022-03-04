import jinja2
import os.path
from bs4 import BeautifulSoup

print("\033[33m   ___  __  ____________  ___  __   ____  _____")
print("  / _ |/ / / /_  __/ __ \/ _ )/ /  / __ \/ ___/")
print(" / __ / /_/ / / / / /_/ / _  / /__/ /_/ / (_ / ")
print("/_/ |_\____/ /_/  \____/____/____/\____/\___/  \033[0m")
print("\nWelcome to Autoblog!")

# open post content and define it as variable

with open ("postcontent.txt", "r") as PostContent:
    post_content=PostContent.read()

# ask for some input from user

post_number = int(input("\nEnter Post Number: "))
post_heading = input("\nEnter a Post Title: ")
post_categories = input("\nEnter post categories (general, news, projects, tutorials)\nseperated by a comma: ")
post_date = input("\nEnter post date (DD.MM.YY): ")

# edit categories to use for classes attribute

post_classes = post_categories.replace(',', '')

# starts a loop to check the actual post number

while True:

    # calculate previous post number

    previous_post_number = post_number - 1

    # check if file already exists so we don't overwrite any posts

    file_exists = os.path.isfile(f'../portfolio/blog-posts/post{post_number}.html') 

    # if file already exists increase postnumber by 1 and restart loop
    # else go to next if statement

    if file_exists:
        print(f"\033[31m\nPost number {post_number} already existed, incresing post index by 1\033[0m")
        post_number += 1
    else:

        # check if previous post exists (i.e. did user skip skip a number?)

        previous_file_exists = os.path.isfile(f'../portfolio/blog-posts/post{post_number - 1}.html') 

        # if previous post exists break loop
        # else reduce postnumber by 1 and restart loop

        if previous_file_exists:
            break
        else:
            print(f"\033[31m\nPrevious post doesn't exist, decreasing post index by 1\033[0m")
            post_number -= 1

# find previous post's title
# parse the previous post's HTML and define it as variable

parsed_html = BeautifulSoup(
    open (f'../portfolio/blog-posts/post{previous_post_number}.html', "r"), "html.parser")

# find the title (text between the h2 tags) and define it as variable

previous_post = parsed_html.find("h2").text

previous_post_name = str(previous_post).strip()
    
# define new post's filename

output_file = f'../portfolio/blog-posts/post{post_number}.html'

# using jinja2 library, pass the variables into the blog template

subs = jinja2.Environment( 
            loader=jinja2.FileSystemLoader('./')      
            ).get_template('post-template.html').render(
                postnumber=post_number,
                postheading=post_heading,
                postdate=post_date,
                postcontent=post_content,
                previouspostnumber=previous_post_number,
                previouspost=previous_post)

# write the new post

with open(output_file,'w') as f: f.write(subs)

print(f"\033[32m\nPost number \033[0m{post_number}\033[32m has been written with title: \033[0m'{post_heading}'")

# Does the user want to add a button to previous post? Loop until answered

while True:
    add_link = input('\nWould you like to add a hyperlink to the previous post? (Y/n) ')

    if add_link == 'Y':

        # write html for "Next →" button

        next_button = BeautifulSoup(
            f"<a href='./post{post_number}.html'><span>Next →</span><span>{post_heading}</span></a>", "html.parser")

        nav_tag = parsed_html.nav

        # insert as the 1st child of previous post's nav tag, break loop

        nav_tag.insert(0, next_button)

        with open(f'../portfolio/blog-posts/post{previous_post_number}.html', 'w') as previouspostfile:
                previouspostfile.write(parsed_html.prettify())

        print(f"\n\033[32mA link has been added to \033[0m'{previous_post_name}'")

        break
    elif add_link == 'n':
        break
    # user inputed invalid answer, restart loop
    else:
        print("\n\033[31mPlease answer with \033[0mY\033[31m for yes, \033[0mn\033[31m for no\033[0m")


# Does the user want to add the post to Archive?

while True:
    add_to_archive = input('\nWould you like to add post to Archive? (Y/n) ')

    if add_to_archive == 'Y':

        # write html to be inserted

        blog_tile = BeautifulSoup(f"\n<a href='./blog-posts/post{post_number}.html' class='blog-tile tile {post_classes}'>\n<h4 class='post-title'>{post_heading}</h4>\n<span class='post-date'>{post_date}</span>\n<span class='post-category'>{post_categories}</span>\n</a>", "html.parser")
        unfiltered_tile = BeautifulSoup(f"\n<a href='./blog-posts/post{post_number}.html' class='unfiltered'>\n<h4 class='post-title'>{post_heading}</h4>\n<span class='post-date'>{post_date}</span>\n<span class='post-category'>{post_categories}</span>\n</a>", "html.parser")

        # parse homepage html

        parsed_archive = BeautifulSoup(open(f'../portfolio/blog.html', 'r'), "html.parser")

        # define blog-tiles div

        blog_tiles = parsed_archive.find(class_="blog-tiles")

        # blog_tiles.insert(0, blog_tile)

        blog_tiles.select_one("div a:nth-of-type(10)").insert_before(unfiltered_tile)

        blog_tiles.select_one("div a:nth-of-type(1)").insert_before(blog_tile)

        with open(f'../portfolio/blog.html', 'w') as blogarchive:
                blogarchive.write(parsed_archive.prettify())

        print(f"\n'{post_heading}'\033[32m has been added to Archive\033[0m")
        break

    elif add_to_archive == 'n':
        break
    else:
        print("\n\033[31mPlease answer with \033[0mY\033[31m for yes, \033[0mn\033[31m for no\033[0m")


# Does the user want to add the post to Recent Posts?

while True:
    add_to_recent = input('\nWould you like to add post to Recent Posts? (Y/n) ')

    if add_to_recent == 'Y':

        # write html to be inserted

        recent_blog_tile = BeautifulSoup(f"\n<a href='./blog-posts/post{post_number}.html' class='blog-tile tile {post_classes}'>\n<h4 class='post-title'>{post_heading}</h4>\n<span class='post-date'>{post_date}</span>\n<span class='post-category'>{post_categories}</span>\n</a>", "html.parser")
        recent_unfiltered_tile = BeautifulSoup(f"\n<a href='./blog-posts/post{post_number}.html' class='unfiltered'>\n<h4 class='post-title'>{post_heading}</h4>\n<span class='post-date'>{post_date}</span>\n<span class='post-category'>{post_categories}</span>\n</a>", "html.parser")

        # parse homepage html

        parsed_homepage = BeautifulSoup(open(f'../portfolio/index.html', 'r'), "html.parser")

        # define blog-tiles div

        recent_blog_tiles = parsed_homepage.find(class_="blog-tiles")

        # insert blog-tile into recent posts div

        recent_blog_tiles.select_one("div a:nth-of-type(7)").insert_before(recent_unfiltered_tile)

        recent_blog_tiles.select_one("div a:nth-of-type(1)").insert_before(recent_blog_tile)

        # remove the oldest post (unfiltered and filtered)

        recent_blog_tiles.select_one("div a:nth-of-type(14)").decompose()

        recent_blog_tiles.select_one("div a:nth-of-type(7)").decompose()

        # write new html document

        with open(f'../portfolio/index.html', 'w') as homepage:
                homepage.write(parsed_homepage.prettify())

        print(f"\n'{post_heading}' \033[32mhas been added to Recent Posts\033[0m")
        print(f"\n\033[32mPost \033[0m{post_number - 6}\033[32m has been removed from Recent Posts\033[0m")

        break

    elif add_to_recent == 'n':
        break
    else:
        print("\n\033[31mPlease answer with \033[0mY\033[31m for yes, \033[0mn\033[31m for no\033[0m")

print("\nAutoblog complete, have a nice day.\n")