VK SignIn Script

#### The script helps to automate your logging into VK

### HOW TO RUN:

*You just need to create _VkSignIn_ class object where you need to provide you login (_email_), password and preferred web driver, one from:*

- ***safari***
- ***chrome***
- ***firefox***

      if __name__ == '__main__':
          sign_in = VkSignIn('your_login', 'your_password', 'web_driver')
          sign_in.signing_in()

*Then you just need to run this command:*

    python run.py

*Or you just can run this script using Docker:*

    docker duild .
    docker run <image id>