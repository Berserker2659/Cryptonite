Author:Uday key : niteCTF{aN_EnCryPteD_DaTAbAsE?}

Player is supposed to use sql cipher and decrypt the database, to do that he will have to decompile the given c# binary, in which he would find that the key is being taken from an webserver with the credentials being hardcoded inside the binary itself. Access the server get the key get the password put that into the binary and that will give you the flag.
