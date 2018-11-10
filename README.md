<h1 align="center">emailpy</h1>
<p align="center">Send email from command line</p>
<p align="center">

## Install


```console
$ git clone https://github.com/nautiyaldeepak/emailpy.git
$ pip3 install -r requirements.txt
$ python3 setup.py install
```

## Usage

```sh
$ emailpy --from senderemail@outlook.com --passwd SenderEmailPassword --to receiveremail@gmail.com --subject "My subject" --message "My message" --attach myattachmentfile
```

#### Examples

```sh
$ emailpy --from senderemail@outlook.com --passwd SenderEmailPassword --to receiveremail@gmail.com --subject "My subject" --message "My message"
Sending email without attachments

$ emailpy --from senderemail@outlook.com --passwd SenderEmailPassword --to receiveremail@gmail.com
Sending a naked email

$ emailpy --from senderemail@outlook.com --passwd SenderEmailPassword --to receiveremail@gmail.com --subject "My subject" --message "My message" --attach mya\
ttachmentfile
Sending email with message, subject & attachments
```

## Note
#### For Gmail Users
If you are using Gmail for sending the otp then there is 1 extra step. You will first has reduce the security of the Gmail Account. Check the Resources section of this Repo to reduce security OR go on the link: https://myaccount.google.com/lesssecureapps The lessSecureAppUse Feature should be "ON".


## Contributing
Do you want to make this better? Open an issue and/or a PR on Github. Thanks!

## License
MIT License

Copyright (c) 2018 [Deepak Nautiyal](https://github.com/nautiyaldeepak)

