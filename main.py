3
B��[�  �               @   s�  d dl mZ d dlmZmZ dZdZdZdZdZ	e
e	� dZd	Zed
ee�j� Zd Z�x$ejdd� ed� �xejddd�D ]�Zdejkr�e
ed e d e d e d ee� d e � e
eeejjdd�� d e � ed� ed7 Zq~dejkr~e
ed e d e d e d ee� d e � e
eeejjdd�� d e � eeejj� d �� ed7 Zq~q~W qXW dS )�    )�sleep)�TelegramClient�syncz[97mz[92mz[0mz[91mz�
################################################
#            @Cryptomierbot Clicker            #
#              BlackHole Security              #
#            14 - September - 2018             #
################################################
i� Z f1cf58739c230b4ca6d27f4ab782b567Z
cryptomierZCryptomierbotu   ⛏ Mine�   �   )�limitzCongratulation!z[+] zSending Request... ZOKz (�)z! z!
�
�x   zPlease wait�   N)Ztimer   Ztelethonr   r   �W�G�N�RZ
__banner__�printZapi_idZapi_hash�startZclient�countZsend_messageZiter_messages�message�str�replace�int�split� r   r   �main.py�<module>   s4   
4" 

4" 
