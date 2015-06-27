|html5-app-compiler|Python script that compiles all resources called in a html web app to make one solid html document|
|---|---|
|Author|Cody Kochmann|
|Modified|Fri Jun 26 22:43:32 2015|

This is a script that compiles all of the pages that are called in a html document and makes one massive html page. The benefit to this is it takes the traditional method of just importing the resources where you need it like in other programming languages and prevents you from needing to waste processor time live rendering the page.

While ajax html construction is nice, apps like tweetdeck or my "3d-css-engine" project have proved that as long as you don't have JavaScript doing insanely intensive things, the app will remain stable even on cheap hardware.

The code blocks are rendered in and out with this method: 

> `addClass("hidden")/removeClass("hidden")`

This project is nice for web apps that are designed like this:

``` html
<!-- side menu code block -->
<style>/* side menu style */</style>
<div><!-- side menu html code --></div>
<script>/* side menu logic */</script>

<!-- options menu code block -->
<style>/* options menu style */</style>
<div><!-- options menu html code --></div>
<script>/* options menu logic */</script>
```

### Upcoming Changes
- add base64 encoding to images being loaded so they are there the instant the code is read.
- add a CLI interphase
- add interval rendering so the compiled document is always up to date.

### Change Log

| Build | Version | Date | Details |
|---|---|---|---|
| 1 | 0.0.1 | 6-26-2015 | First public build. |


