
a1877@Hanxr MINGW64 ~
$ ssh-keygen -t rsa -c "1224834309@qq.com"
Too many arguments.
usage: ssh-keygen [-q] [-b bits] [-t dsa | ecdsa | ed25519 | rsa]
                  [-N new_passphrase] [-C comment] [-f output_keyfile]
       ssh-keygen -p [-P old_passphrase] [-N new_passphrase] [-f keyfile]
       ssh-keygen -i [-m key_format] [-f input_keyfile]
       ssh-keygen -e [-m key_format] [-f input_keyfile]
       ssh-keygen -y [-f input_keyfile]
       ssh-keygen -c [-P passphrase] [-C comment] [-f keyfile]
       ssh-keygen -l [-v] [-E fingerprint_hash] [-f input_keyfile]
       ssh-keygen -B [-f input_keyfile]
       ssh-keygen -D pkcs11
       ssh-keygen -F hostname [-f known_hosts_file] [-l]
       ssh-keygen -H [-f known_hosts_file]
       ssh-keygen -R hostname [-f known_hosts_file]
       ssh-keygen -r hostname [-f input_keyfile] [-g]
       ssh-keygen -G output_file [-v] [-b bits] [-M memory] [-S start_point]
       ssh-keygen -T output_file -f input_file [-v] [-a rounds] [-J num_lines]
                  [-j start_line] [-K checkpt] [-W generator]
       ssh-keygen -s ca_key -I certificate_identity [-h] [-n principals]
                  [-O option] [-V validity_interval] [-z serial_number] file ...
       ssh-keygen -L [-f input_keyfile]
       ssh-keygen -A
       ssh-keygen -k -f krl_file [-u] [-s ca_public] [-z version_number]
                  file ...
       ssh-keygen -Q -f krl_file file ...

a1877@Hanxr MINGW64 ~
$ ssh-keygen -t rsa -C "1224834309@qq.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/a1877/.ssh/id_rsa):
Created directory '/c/Users/a1877/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /c/Users/a1877/.ssh/id_rsa.
Your public key has been saved in /c/Users/a1877/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:RwkqARVdRmNJz6aUTsIkz9SjD1D9QKMGd14ZL2WCwYk 1224834309@qq.com
The key's randomart image is:
+---[RSA 2048]----+
|  .o*+=X&=+oo    |
|    .@EBXO.*     |
|    ..O.=+B .    |
|     oo= +..     |
|       oS .      |
|        ..       |
|                 |
|                 |
|                 |
+----[SHA256]-----+

a1877@Hanxr MINGW64 ~
$ cd G:

a1877@Hanxr MINGW64 /g
$ cd learngit

a1877@Hanxr MINGW64 /g/learngit (master)
$ git remote add origin git@github.com:Hanxiaorong/learngit

a1877@Hanxr MINGW64 /g/learngit (master)
$ git push -u origin master
The authenticity of host 'github.com (192.30.255.113)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no)?
Host key verification failed.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

a1877@Hanxr MINGW64 /g/learngit (master)
$ git remote add origin git@github.com:Hanxiaorong/learngit.git
fatal: remote origin already exists.

a1877@Hanxr MINGW64 /g/learngit (master)
$ rmdir remote origin
rmdir: failed to remove 'remote': No such file or directory
rmdir: failed to remove 'origin': No such file or directory

a1877@Hanxr MINGW64 /g/learngit (master)
$ git remote add origin https://github.com/Hanxiaorong/learngit.git
fatal: remote origin already exists.

a1877@Hanxr MINGW64 /g/learngit (master)
$ ^C

a1877@Hanxr MINGW64 /g/learngit (master)
$ git remote rm origin

a1877@Hanxr MINGW64 /g/learngit (master)
$ git remote add origin https://github.com/Hanxiaorong/learngit.git

a1877@Hanxr MINGW64 /g/learngit (master)
$ git push -u origin master
Counting objects: 24, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (21/21), done.
Writing objects: 100% (24/24), 2.04 KiB | 1.02 MiB/s, done.
Total 24 (delta 8), reused 0 (delta 0)
remote: Resolving deltas: 100% (8/8), done.
To https://github.com/Hanxiaorong/learngit.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.

a1877@Hanxr MINGW64 /g/learngit (master)
$ cd ..

a1877@Hanxr MINGW64 /g
$ cd github

a1877@Hanxr MINGW64 /g/github
$ cd learngit

a1877@Hanxr MINGW64 /g/github/learngit (master)
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    hei.txt

no changes added to commit (use "git add" and/or "git commit -a")

a1877@Hanxr MINGW64 /g/github/learngit (master)
$ cd ../

a1877@Hanxr MINGW64 /g/github
$ cd py101-004

a1877@Hanxr MINGW64 /g/github/py101-004 (master)
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

nothing to commit, working tree clean

a1877@Hanxr MINGW64 /g/github/py101-004 (master)
$ cd ../

a1877@Hanxr MINGW64 /g/github
$ cd ../

a1877@Hanxr MINGW64 /g
$ cd learnpython

a1877@Hanxr MINGW64 /g/learnpython
$ cd ex2
bash: cd: ex2: No such file or directory

a1877@Hanxr MINGW64 /g/learnpython
$ cd task

a1877@Hanxr MINGW64 /g/learnpython/task
$ cd ch3

a1877@Hanxr MINGW64 /g/learnpython/task/ch3
$ git add hello.py
fatal: Not a git repository (or any of the parent directories): .git

a1877@Hanxr MINGW64 /g/learnpython/task/ch3
$ cd ../../../

a1877@Hanxr MINGW64 /g
$ cd github

a1877@Hanxr MINGW64 /g/github
$ cd py101-004

a1877@Hanxr MINGW64 /g/github/py101-004 (master)
$ cd add hello.py
bash: cd: too many arguments

a1877@Hanxr MINGW64 /g/github/py101-004 (master)
$ git add hello.py
fatal: pathspec 'hello.py' did not match any files

a1877@Hanxr MINGW64 /g/github/py101-004 (master)
$ cd ch3
bash: cd: ch3: No such file or directory

a1877@Hanxr MINGW64 /g/github/py101-004 (master)
$ cd chap3

a1877@Hanxr MINGW64 /g/github/py101-004/chap3 (master)
$ cd project

a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
$ git add hello.py

a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   hello.py


a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
$ git diff

a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
$ git push origin master
To https://github.com/Hanxiaorong/Py101-004.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/Hanxiaorong/Py101-004.git                                                                                                                                  '
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
$ git commit -m "a new file"
[master 8e72ba3] a new file
 1 file changed, 20 insertions(+)
 create mode 100644 Chap3/project/hello.py

a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
$ git add hello.py

a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
$ git commit -m 'hello_world'
[master cde7b5a] hello_world
 1 file changed, 2 insertions(+)

a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
$ git diff hello.py

a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
$ git status
On branch master
Your branch is ahead of 'origin/master' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
$ git log
commit cde7b5af302fec1539eff716384206fd0a019fcc (HEAD -> master)
Author: Hanxiaorong <1224834309@qq.com>
Date:   Sun Sep 3 23:05:17 2017 +0800

    hello_world

commit 8e72ba3bec19b13ea23a060d16776ca5cae05940
Author: Hanxiaorong <1224834309@qq.com>
Date:   Sun Sep 3 23:03:39 2017 +0800

    a new file

commit e351ff2af869b270f4978246a66867faef4491ca (origin/master, origin/HEAD)
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Tue Aug 22 11:30:36 2017 +0800

    Add files via upload

commit 1d375c121930924283e045cc6adcefc13edd2f9c
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Tue Aug 22 11:18:09 2017 +0800

    Add files via upload

commit b0236d0c4b520ced05defc3499fd4dd97a0ca3de
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Mon Aug 21 23:28:57 2017 +0800

    Add files via upload

commit b4c67f8c727bb25f8912b6a0733244e6f7b2cd01
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sun Aug 13 23:40:23 2017 +0800

    Add files via upload

commit e684022e5f558b9a2a5d1857174ba7a8d0a43834
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sun Aug 13 23:06:03 2017 +0800

    Add files via upload

commit bc86d4376e111f65176b339f726fcbea34c54776
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sun Aug 13 22:54:57 2017 +0800

    Add files via upload

commit 078b47b51c6204793c17be978f6c3b0736269cce
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sun Aug 13 22:53:24 2017 +0800

    更新

commit c293793a30c2536cecaf42be25396e20b4ec106e
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sun Aug 13 17:26:53 2017 +0800

    Add files via upload

commit f3bf78a821d0c2fa8bd2284eafdb611453dd4460
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sun Aug 13 17:15:58 2017 +0800

    Update 说明

commit 182d8dcc7605e5284d6e12ed7114c95a08877176
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sun Aug 13 17:14:38 2017 +0800

    Delete 教程

commit 685fc0c0ce6d4fca7bf5b8e842079073b92ed753
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sun Aug 13 17:14:21 2017 +0800

    Create 说明

commit 34af9109ef96d05288702376c453867e991fe856
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sun Aug 13 17:05:43 2017 +0800

    Create 教程

commit ba0c73c1f6db438a31c8b892131257e456019176
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sun Aug 13 17:04:46 2017 +0800

    Delete Jupyter notebook 入门简介-checkpoint.ipynb

commit be546be981565a645040de9012a45c3ba87de003
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sun Aug 13 16:56:37 2017 +0800

    Add files via upload

commit dd70b569778ce51ecdba28dd04125ebea71e7e5d
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sun Aug 13 16:26:34 2017 +0800

    Add files via upload

commit 82342ce6a85d94230fe9a215304c90bd13568f2c
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sun Aug 13 16:25:47 2017 +0800

    Add files via upload

commit 42af8996483c065a3ba895b1663bdd13add3338d
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sun Aug 13 16:24:55 2017 +0800

    Add files via upload

commit 1cc0337fdeb875aa098f7bce9c2cc6e270d4ed38
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sun Aug 13 00:28:58 2017 +0800

    Delete 学习小结.txt

commit c031162fcb4eedb009b153ee15bb006532b19942
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sat Aug 12 19:47:56 2017 +0800

    习题35

commit 8bf48376d6b0f9aa8268a87e714e8474f68f2c7c
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sat Aug 12 19:47:08 2017 +0800

    习题32

commit b79b12ebb17d28518e47c725687ccb70a7f05019
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sat Aug 12 19:44:33 2017 +0800

    习题21

commit fd9cf7a3988619f8af397ad3cdd1540f7d0c622e
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sat Aug 12 19:43:57 2017 +0800

    习题13

commit 15cf1f862214329c2a7a122b8167152a6368054b
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sat Aug 12 19:42:55 2017 +0800

    习题10

commit c4387f70aa0ec7f8faadeb8754715bedb481c6ac
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sat Aug 12 19:42:21 2017 +0800

    习题9

commit 2dc4b6a23d2b3dc1234ca2001423f88bcf386bfb
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sat Aug 12 19:41:34 2017 +0800

    习题6

commit 46a2de8fd6e1aca3220aa9c7d9107b0cd41f2dc2
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sat Aug 12 19:40:47 2017 +0800

    习题3

commit 4c129c8ec5a01f7b6008a9c5fa8e7d7b12f82238
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Sat Aug 12 19:40:18 2017 +0800

    习题1

commit e57ae72aa2fbb640b988f53eb5b8119ca05dd71e
Author: Hanxiaorong <30439925+Hanxiaorong@users.noreply.github.com>
Date:   Thu Aug 10 21:37:19 2017 +0800

    随便试试

commit 2e6ecd098a976a07652af06c57cba080095f8dd5
Author: iamzhuoxuan <iamzhuoxuan@gmail.com>
Date:   Fri Aug 4 19:30:06 2017 +0800

    Py101-004 init.

commit 6c34ce3d653cd1f0b9482d0de40d18a6eaea00bb
Author: AICourseOMC <AICourse@openmindclub.com>
Date:   Thu Jul 6 19:38:41 2017 +0800

    Initial commit
(END)

a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
git push origin master
To https://github.com/Hanxiaorong/Py101-004.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/Hanxiaorong/Py101-004.git                                                                                                                                  '
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
$ git push origin master
To https://github.com/Hanxiaorong/Py101-004.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/Hanxiaorong/Py101-004.git                                                                                                                                  '
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
$ git remote add origin https://github.com/Hanxiaorong/py101-004.py
fatal: remote origin already exists.

a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
$ git remote rm origin

a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
$ ^C

a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
$ git remote add origin https://github.com/Hanxiaorong/py101-004.py

a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
$ cd ../../

a1877@Hanxr MINGW64 /g/github/py101-004 (master)
$ git remote add origin https://github.com/Hanxiaorong/py101-004.py
fatal: remote origin already exists.

a1877@Hanxr MINGW64 /g/github/py101-004 (master)
$ git remote origin
error: Unknown subcommand: origin
usage: git remote [-v | --verbose]
   or: git remote add [-t <branch>] [-m <master>] [-f] [--tags | --no-tags] [--m                                                                                                                                  irror=<fetch|push>] <name> <url>
   or: git remote rename <old> <new>
   or: git remote remove <name>
   or: git remote set-head <name> (-a | --auto | -d | --delete | <branch>)
   or: git remote [-v | --verbose] show [-n] <name>
   or: git remote prune [-n | --dry-run] <name>
   or: git remote [-v | --verbose] update [-p | --prune] [(<group> | <remote>)..                                                                                                                                  .]
   or: git remote set-branches [--add] <name> <branch>...
   or: git remote get-url [--push] [--all] <name>
   or: git remote set-url [--push] <name> <newurl> [<oldurl>]
   or: git remote set-url --add <name> <newurl>
   or: git remote set-url --delete <name> <url>

    -v, --verbose         be verbose; must be placed before a subcommand


a1877@Hanxr MINGW64 /g/github/py101-004 (master)
$ git remote rm origin

a1877@Hanxr MINGW64 /g/github/py101-004 (master)
$ git remote add origin https://github.com/Hanxiaorong/py101-004.py

a1877@Hanxr MINGW64 /g/github/py101-004 (master)
$ git push origin master
remote: Repository not found.
fatal: repository 'https://github.com/Hanxiaorong/py101-004.py/' not found

a1877@Hanxr MINGW64 /g/github/py101-004 (master)
$ git remote add origin https://github.com/Hanxiaorong/py101-004.py
fatal: remote origin already exists.

a1877@Hanxr MINGW64 /g/github/py101-004 (master)
$ git remote rm origin

a1877@Hanxr MINGW64 /g/github/py101-004 (master)
$ git remote add origin https://github.com/Hanxiaorong/py101-004.git

a1877@Hanxr MINGW64 /g/github/py101-004 (master)
$ git push -u origin master
To https://github.com/Hanxiaorong/py101-004.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/Hanxiaorong/py101-004.git                                                                                                                                  '
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

a1877@Hanxr MINGW64 /g/github/py101-004 (master)
$ git pudh --help
git: 'pudh' is not a git command. See 'git --help'.

The most similar command is
        push

a1877@Hanxr MINGW64 /g/github/py101-004 (master)
$ git push --help

a1877@Hanxr MINGW64 /g/github/py101-004 (master)
$ cd ../

a1877@Hanxr MINGW64 /g/github
$ cd github
bash: cd: github: No such file or directory

a1877@Hanxr MINGW64 /g/github
$ cd learngit

a1877@Hanxr MINGW64 /g/github/learngit (master)
$ git diff
diff --git a/hei.txt b/hei.txt
deleted file mode 100644
index fa81419..0000000
--- a/hei.txt
+++ /dev/null
@@ -1 +0,0 @@
-<D0>޸<C4><CE>ļ<FE>
\ No newline at end of file

a1877@Hanxr MINGW64 /g/github/learngit (master)
$ git statuss
git: 'statuss' is not a git command. See 'git --help'.

The most similar command is
        status

a1877@Hanxr MINGW64 /g/github/learngit (master)
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    hei.txt

no changes added to commit (use "git add" and/or "git commit -a")

a1877@Hanxr MINGW64 /g/github/learngit (master)
$ cd ../

a1877@Hanxr MINGW64 /g/github
$ cd py101-004

a1877@Hanxr MINGW64 /g/github/py101-004 (master)
$ cd chap3

a1877@Hanxr MINGW64 /g/github/py101-004/chap3 (master)
$ cd project

a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
$ git push -u origin master
To https://github.com/Hanxiaorong/py101-004.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://github.com/Hanxiaorong/py101-004.git                                                                                                                                  '
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

a1877@Hanxr MINGW64 /g/github/py101-004/chap3/project (master)
$ cd ../../../

a1877@Hanxr MINGW64 /g/github
$ cd learngit

a1877@Hanxr MINGW64 /g/github/learngit (master)
$ git push -u origin master
Everything up-to-date
Branch master set up to track remote branch master from origin.

a1877@Hanxr MINGW64 /g/github/learngit (master)
$ 
