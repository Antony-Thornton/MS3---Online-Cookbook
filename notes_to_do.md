
Steps to fix form refresh issue. The issue where when a duplicate form is created the page is refreshed and the data on the form is lost. Not very helpful if the user has written a lot in the instructions.

1- set up and event listener to the submit button
2- prevent the page from relaoding
3- create a fetch post request from the form data
4, submit to the backend
5. in the backend perform your checks
6. if the post exist already, return a JSON HTTP response to the promise of the fetch function and parse the json data
7. write to the dom the title already exist and that the user should change it.