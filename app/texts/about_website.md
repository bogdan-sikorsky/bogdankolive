# About website

**[GitHub](https://github.com/bogdan-sikorsky/bogdanko_live)**

This page is dedicated to a story about the idea behind the website and its technical details

---

### Purpose

Everyone is familiar with an issue when you're talking with clients or recruiters and they ask to show your CV, portfolio etc. I previously stored my resume in a nicely formatted Google Doc file and I was able to share it by the link.

I like to update my resume frequently and it was a problem for me. Sometimes I need to send my CV as a file and not as a link so each time I had to download a CV. I always had a slightly different version. Files were stuck over each other and in a matter of time, I had dozens of PDF files with my CV across multiple devices. That was a real mess.

<img src="https://raw.githubusercontent.com/bogdan-sikorsky/icons/main/bogdansikorsky/cat_code_02.jpeg" alt="niceimage" style="border-radius:5%" border="0">

#####

Meanwhile, you can't add to your resume a lot of background and context about yourself since it should be short if possible so I needed a place alongside the CV to add this context. Also, it is important to have a place with something kinda of portfolio. So I decided to create my own website to have it all in one place, have easy and simple access to edit it and have one and only up-to-date version of my CV that anyone can review and download if needed.

# Technical requirements

### Text editing

First of all, I needed to be able to have easy access to edit my text without admin panels and dozens of different fields. I needed to have something as simple as Google Docs but not limited to A4 format because it was hard to integrate it with a style.

Markdown files become the best solution for me because they are easy to integrate and are as easily editable as Docs if you spend 30 minutes learning.

### Web application

I'm not a front-end fella or a designer, at least for now so I needed a Python framework that would minimize my interactions with HTML, CSS or JavaScript.

Fortunately, in 2024 there are plenty of Python frameworks that give you a chance to make your web app with frontend but to use Python only.

I've chosen Stearmlit since it looked to me as the simplest one, reliable since it has been maintained for multiple years, has its community if questions arise and is well documented. As a side note, this framework is a very powerful tool for infographics, dashboards etc. so it was nice to learn it in action.

# How it works

### Markdown

All the text you see on any page of this website is typed in Markdown files. You can find them in on my [GitHub Repo](https://github.com/bogdan-sikorsky/bogdanko_live/tree/main/app/texts). It is as simple as possible. I do my edits, committing them to GitHub and I'm always up to date.

### Streamlit

Stermlit works as my back-end and front-end at the same time. It is very simple to use if you have never before worked with front-end. You need one line of code for Strearmlit to parse Markdown to your page. If you're not in charge of beauty and have something relatively small you can make your app in an hour. Stearmlit will make everything for you.

Meanwhile, this simplicity has its downsides.

> Your front-end is quite scripted and if you want to make it beautiful and customize it for yourself you'll probably have to spend time learning how the framework works and manually change what you want.

> I had to find in framework index.html and replace it with my own to use my own logo, website name and website description in link previews in chats and Google indexing. By default, index.html contains Stearmlit branding that appears everything even if you used built-in commands to change those.

> I had to inject a bit of my own CSS to remove some unnecessary features for my personal website, increase font size etc.

> It looks to me that it is not possible to make a dynamic routing with this framework but I don't need multiple pages with stuff like some products so it is fine for me.

### Standardized environments

Nothing new and special. I have quite simple Docker and Docker-Compose files to distribute my app across multiple machines and not to be worried that something will fail.

### Server

This website is deployed on Amazon Web Services EC2 machinery.

To organize server routing I used a simple but yet powerful tool called Traefik that directs incoming traffic to the Streamlit app. Also, I used Cloudflare to get an SSL certificate.

### CI/CD

I have a GitHub workflow that handles all deployment processes so all I need to do to edit something is commit changes to Git. Everything else GitHub will handle for me.

### Health monitoring

I have 3 tools that help me monitor how healthy my website is.

- Sentry gathers reports about any inside app errors and sends reports to my email if there are any issues.
- I use a very powerful tool called NetData that shows me how healthy my server is (CPU, Memory, Storage etc.).
- The UptimeRobot checks if my website is online every 5 minutes and will send an email notification if my website does not respond. 

### Analytics

I use Google Analytics and brand new for me tools that called LogRocket and PostHog to be up to date how popular my website is.

Some statistics provides also Cloudflare which I use for SSL certificates.

# Conclusion

In the end, this setup has given me exactly what I wanted: a simple, centralized platform to share my CV, add context about myself, and display my portfolio without the hassle of multiple file versions or cluttered devices. The combination of Markdown for easy text editing and Streamlit for both back-end and front-end functionality has made managing and updating my site straightforward and fast.

Yes, there were some tweaks needed—like injecting custom CSS and swapping out the default `index.html`— but these were minor compared to the overall benefits. Deploying everything using Docker, routing traffic with Traefik, and relying on GitHub Actions for CI/CD has automated the majority of the tedious parts, leaving me with a smooth, always up-to-date website.

While Streamlit’s flexibility may not cater to more complex, multi-page applications, it works perfectly for my needs — a personal website to showcase my CV, background, and portfolio all in one place, with minimal maintenance and maximum accessibility.

#### You always can check this project's GitHub repository by this [link](https://github.com/bogdan-sikorsky/bogdanko_live).
