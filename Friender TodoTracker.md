# Friender Todo Tracker

## Minimum Viable Product Stage

### Project Structure

- │ = ALT + 179
- └ = ALT + 192
- ├ = ALT + 195
- ─ = ALT + 196

``` arduino
Friender/
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── users/
│   │   ├── edit.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── profile.html
│   │   └── signup.html
│   │
│   ├── _form.html
│   ├── 404.html
│   ├── base.html
│   ├── home-anon.html
│   └── home.html
│
├── models.py
├── routes.py
├── forms.py
│
├── app.py
├── requirements.txt
└── README.md
```

### [x] **Landing Page for Non-Logged-in Users**

- [x] Create a landing page that welcomes users and provides basic information about the platform.
- [x] Include a call-to-action button or link to the signup page.

### [x] **Homepage for Logged-in Users**

- [x] Develop a homepage layout for users who are logged in.
- [x] Display relevant information or actions such as profile updates, friend suggestions, or recent activity.

### [x] **Login Page**

- [x] Design a login page with fields for username and password.
- [x] Implement authentication logic to validate user credentials.
- [x] Include a link to the signup page for new users.

### [x] **Signup Page**

- [x] Create a signup form with fields for username, password, email, phone number, friend radius, profile photo, first name, and last name.
- [x] Implement form validation to ensure all required fields are filled.
- [x] Set up logic to create a new user account upon submission.

### [ ] **Profile Page**

- [x] Design a profile page layout displaying user information in a bootstrap card format.
- [x] Include the user's profile photo, username, first name, last name, list of hobbies, list of interests, edit button, delete button.
- [x] Ensure that only the profile owner can view and edit their profile.
- [ ] Implement delete route functionality

### [ ] **Users Page**

- [ ] Develop a page to display cards of all users on the site.
- [ ] Each card should include the user's profile photo, username, first name, list of hobbies, and list of interests.
- [ ] Enable users to click on a card to navigate to the respective user's profile page.

### [x] **CSRF Protection Form**

- [x] CSRF Protection form implemented

### [x] **User Login Form**

- [x] Create a form for users to login.
- [x] username, password

### [x] **User Signup Form**

- [x] Create a form for users to signup.
- [x] username, first_name, last_name, email, password, phone_number, zipcode

### [x] **Profile Edit Form**

- [x] Create a form for users to edit their profile information.
- [x] Allow users to upload a profile photo, modify their friend radius, update zipcode, and add interests and hobbies from dropdown lists.
- [x] Implement validation to handle edits appropriately.

### [x] **S3 Bucket Integration**

- [x] Use file input from Profile Edit form to save user submitted profile photo file to S3
- [x] Ensure that permissions allow read/write access to S3
- [x] Ensure read on /users, /users/<username> accesses profile photo correctly

### [ ] **Routing and Navigation**

- [x] Set up routing logic to navigate between different pages of the application.
- [x] Ensure proper redirection based on user actions such as login, signup, profile edit, etc.
- [ ] Delete route functionality

### [ ] **Styling and UI Enhancement**

- [ ] Apply CSS styling to improve the visual appearance and user experience of the pages.
- [ ] Ensure consistency in design elements across the application.

### Notable Bugs
