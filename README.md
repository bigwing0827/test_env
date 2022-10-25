# いろいろテストした場

## git clone https://github.com/bigwing0827/test_env.git

## git push
2021年8月13日から、ローカルからGithubにアクセスする際にパスワードではなく、個人アクセストークンが必要になった。
https://ios-docs.dev/20210813support-for-password/
https://qiita.com/atsymd/items/a1ff5a496b78f47ce80e

現在のOriginを削除
```
git remote remove origin
```
トークン認証用のOriginURLを追加。
```
git remote add origin https://<トークン>@github.com/<ユーザ>/<リポジトリ>.git
git remote add origin https://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@github.com/bigwing0827/test_env.git
```
git push --set-upstream origin master