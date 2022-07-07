from re import sub
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import os

class Util:

	@staticmethod
	def send_email(data):
		html_template='message.html'
	
		html_content = render_to_string(html_template, {'context':data['content']}) 
		
		text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.
	
		msg = EmailMultiAlternatives( data['subject'],text_content ,'charityxx123@gmail.com' , data['to_email'])
		
		msg.attach_alternative(html_content, "text/html")
		
		msg.send()	

	def send_email_pass(data):
		html_template='reset.html'
		html_content = render_to_string(html_template, {'context':data['content']}) 
		text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.
		msg = EmailMultiAlternatives( data['subject'],text_content ,'charityxx123@gmail.com' , data['to_email'])
		msg.attach_alternative(html_content, "text/html")
		msg.send() 


        
		
