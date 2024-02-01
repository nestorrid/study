静态博客框架整理
================================================

Pelican
    基于python实现的静态博客站点生成器. https://getpelican.com/

    .. code-block:: bash

        # 安装
        python -m pip install "pelican[markdown]"

        # 创建项目
        mkdir -p ~/projects/yoursite
        cd ~/projects/yoursite
        pelican-quickstart

        # 创建文章
        # ~/projects/yoursite/content/keyboard-review.md

        # Title: My First Review
        # Date: 2010-12-03 10:20
        # Category: Review

        # Following is a review of my favorite mechanical keyboard.

        # 预览
        pelican -r -l

    `Pelican文档 <https://docs.getpelican.com/en/latest/quickstart.html>`_
    `pelican插件 <https://github.com/orgs/pelican-plugins/repositories?type=all>`_
    `pelican主题 <https://github.com/getpelican/pelican-themes>`_

hexo.io
    基于Node.js的静态博客框架, 插件丰富, 部署简单. https://hexo.io/zh-cn/

    .. code-block:: bash

        npm install hexo-cli -g
        hexo init blog
        cd blog
        npm install
        hexo server

    `hexo地址 <https://hexo.io/zh-cn/docs/>`_

VuePress
    基于vue的静态博客框架. 感觉不错, 但是目前的可用主题和资源不是太多. https://v2.vuepress.vuejs.org/

    `VuePress文档地址 <https://v2.vuepress.vuejs.org/guide/getting-started.html>`_
    `npm社区主题 <https://www.npmjs.com/search?q=keywords:vuepress-theme>`_
    `hope主题 <https://theme-hope.vuejs.press/demo/project-home.html>`_

docsify
    比较适合制作静态文档, 不是太适合做博客. https://docsify.js.org/