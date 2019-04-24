<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<!-- saved from url=(0134)https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html -->
<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

      <title>sam local
         generate-event - AWS Serverless Application Model
      </title>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="home" href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html#top">
      <link rel="up" href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html" title="AWS SAM CLI Command Reference">
      <link rel="prev" href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-init.html" title="sam init">
      <link rel="next" href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-invoke.html" title="sam local invoke">
      <meta name="description" content="Generates sample payloads from different event sources, such as Amazon S3, Amazon API Gateway, and Amazon SNS. These payloads contain the information that the event sources send to your Lambda functions.">
      <meta name="keywords" content="AWS Serverless Application Model,Serverless Application Model,AWS SAM,SAM,AWS SAM CLI,SAM CLI,serverless applications,serverless,cloud computing,Lambda,API Gateway,CloudFormation,deployment,CI/CD,local testing,local">
      <meta name="deployment_region" content="IAD">
      <meta name="product" content="AWS Serverless Application Model">
      <meta name="guide" content="Developer Guide">
      <meta name="guide-locale" content="en_us">
      <meta name="tocs" content="toc-contents.json">
      <link rel="icon" type="image/ico" href="https://docs.aws.amazon.com/images/favicon.ico">
      <link rel="shortcut icon" type="image/ico" href="https://docs.aws.amazon.com/images/favicon.ico">
      <link rel="canonical" href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html">
      <link rel="stylesheet" type="text/css" href="./sam local generate-event_files/jquery-ui.min.css">
      <link rel="stylesheet" type="text/css" href="./sam local generate-event_files/font-awesome.min.css">
      <link rel="stylesheet" type="text/css" href="./sam local generate-event_files/google-font.css">
      <link id="code-style" rel="stylesheet" type="text/css" href="./sam local generate-event_files/light.css">
      <link rel="stylesheet" type="text/css" href="./sam local generate-event_files/jquery-ui.theme.css">
      <link rel="stylesheet" type="text/css" href="./sam local generate-event_files/colorbox.css">
      <link rel="stylesheet" type="text/css" href="./sam local generate-event_files/awsdocs.css"><script type="text/javascript" src="./sam local generate-event_files/highlight.pack.js"></script><script type="text/javascript" src="./sam local generate-event_files/jquery.min.js"></script><script type="text/javascript" src="./sam local generate-event_files/jquery-ui.min.js"></script><script type="text/javascript" src="./sam local generate-event_files/jquery.colorbox.js"></script><script type="text/javascript" src="./sam local generate-event_files/awsdocs.min.js"></script></head>
   <body id="top">
      <div xmlns:db="http://docbook.org/ns/docbook" id="aws-nav" class="aws-nav-header">
         <div class="aws-nav-header-left">
            <div class="aws-nav-logo">
               <!--aws_logo_105x39.png--><a href="http://aws.amazon.com/"><img src="./sam local generate-event_files/aws_logo_105x39.png" alt="Amazon Web Services"></a></div>
         </div>
         <div id="aws-nav-header-right" class="aws-nav-header-right">
            <div class="aws-nav-cta-button-outer"><a id="aws-nav-cta-button" class="aws-nav-button" href="https://console.aws.amazon.com/console/home">Sign In to the Console</a></div>
            <div class="aws-nav-popover-trigger" data-dropdown="aws-nav-dropdown-lang"><select id="languageSelection" onchange="SelectLanguage()" style="display: none;">
                  <option value="/de_de/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html">Deutsch</option>
                  <option value="/en_us/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html" selected="selected">English</option>
                  <option value="/es_es/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html">Español</option>
                  <option value="/fr_fr/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html">Français</option>
                  <option value="/it_it/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html">Italiano</option>
                  <option value="/ja_jp/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html">日本語</option>
                  <option value="/ko_kr/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html">한국어</option>
                  <option value="/pt_br/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html">Português</option>
                  <option value="/zh_cn/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html">中文 (简体)</option>
                  <option value="/zh_tw/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html">中文 (繁體)</option></select><span tabindex="0" id="languageSelection-button" role="combobox" aria-expanded="false" aria-autocomplete="list" aria-owns="languageSelection-menu" aria-haspopup="true" class="ui-selectmenu-button ui-selectmenu-button-closed ui-corner-all ui-button ui-widget"><span class="ui-selectmenu-icon ui-icon ui-icon-triangle-1-s"></span><span class="ui-selectmenu-text">English</span></span></div><a class="btn btn-rss-link" id="rss-link-top" target="_blank" href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-application-model-updates.rss" title="View RSS Feed"></a><a class="btn btn-kindle-link" id="kindle-link-top" target="_blank" href="http://www.amazon.com/dp/B07P7K9VZB" title="Open Kindle"></a><a class="btn btn-pdf-link" id="pdf-link-top" href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-application-model.pdf#sam-cli-command-reference-sam-local-generate-event" target="_blank" title="Open PDF"></a><a class="btn btn-github-link" id="github-link-top" href="https://github.com/awsdocs/aws-sam-developer-guide/tree/master/doc_source/sam-cli-command-reference-sam-local-generate-event.md" target="_blank" title="Edit on GitHub"></a><div id="aws-nav-quicklinks-separator" class="aws-nav-quicklinks-separator">
               <div class="aws-nav-left"></div>
               <div class="aws-nav-right"></div>
            </div>
         </div>
      </div>
      <div id="content-container">
         <div id="left-column" class="ui-resizable">
            <div id="left-col-header">
               <div xmlns:db="http://docbook.org/ns/docbook" id="left-col-top-content">
                  <div id="service-name">AWS Serverless Application Model </div>
                  <div id="search"><i id="search-icon" class="fa fa-search fa-2x"></i></div>
                  <div id="guide-info">Developer Guide
                     <div id="content-button"><i id="toggle-contents" class="fa fa-bars"></i></div>
                  </div>
               </div>
               <form id="finegrainedSearch" method="get" onsubmit="return searchFormSubmit(this);" action="https://docs.aws.amazon.com/search/doc-search.html">
                  <div id="search-form"><select id="search-select" name="searchPath">
                        <option value="all">Entire Site</option>
                        <option value="AWSMarketplace">AMIs from AWS Marketplace</option>
                        <option value="amis">AMIs from All Sources</option>
                        <option value="articles">Articles &amp; Tutorials</option>
                        <option value="products_and_info">AWS Product Information</option>
                        <option value="case_studies">Case Studies</option>
                        <option value="customerapps">Customer Apps</option>
                        <option value="documentation">Documentation</option>
                        <option value="documentation-product">Documentation - This Product</option>
                        <option value="documentation-guide" selected="selected">Documentation - This Guide</option>
                        <option value="datasets">Public Data Sets</option>
                        <option value="releasenotes">Release Notes</option>
                        <option value="solution_providers">Partners</option>
                        <option value="code">Sample Code &amp; Libraries</option></select><br><input id="search-query" name="searchQuery" type="text" placeholder="Search"><input id="search-button" src="./sam local generate-event_files/search-button.png" alt="Go" type="image"></div><input type="hidden" name="this_doc_product" id="this_doc_product" value="AWS Serverless Application Model"><input type="hidden" name="this_doc_guide" id="this_doc_guide" value="Developer Guide"><input type="hidden" name="doc_locale" value="en_us"></form>
            </div>
            <div id="toc"><ul class="awstoc opened"><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html" class="awstoc">What Is AWS SAM?</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-quick-start.html" class="awstoc">Quick Start</a></li><li class="awstoc closed"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-basics.html" class="awstoc">AWS SAM Template Concepts</a><ul class="awstoc"><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template.html" class="awstoc">Declaring Serverless Resources</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/appendix-appendix-sam-templates-and-cf-templates.html" class="awstoc">Declaring AWS CloudFormation Resources</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-nested-applications.html" class="awstoc">Nested Applications</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-controlling-access-to-apis.html" class="awstoc">Controlling Access to APIs</a></li></ul></li><li class="awstoc closed"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-test-and-debug.html" class="awstoc">Testing and Debugging Serverless Applications</a><ul class="awstoc"><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-build.html" class="awstoc">Building Applications with Dependencies</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-invoke.html" class="awstoc">Invoking Functions Locally</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-start-api.html" class="awstoc">Running API Gateway Locally</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-layers.html" class="awstoc">Working with Layers</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-automated-tests.html" class="awstoc">Running Automated Tests</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-generate-event.html" class="awstoc">Generating Sample Event Payloads</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html" class="awstoc">Working with Logs</a></li><li class="awstoc closed"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-debugging.html" class="awstoc">Step-Through Debugging Lambda Functions Locally</a><ul class="awstoc"><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-debugging-nodejs.html" class="awstoc">Node.js</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-debugging-python.html" class="awstoc">Python</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-debugging-golang.html" class="awstoc">Golang</a></li></ul></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-debugging-additional-arguments.html" class="awstoc">Passing Additional Runtime Debug Arguments</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-validate.html" class="awstoc">Validating AWS SAM Template Files</a></li></ul></li><li class="awstoc closed"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-deploying.html" class="awstoc">Deploying Serverless Applications</a><ul class="awstoc"><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/automating-updates-to-serverless-apps.html" class="awstoc">Gradual Code Deployment</a></li></ul></li><li class="awstoc closed"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications.html" class="awstoc">Publishing Serverless Applications</a><ul class="awstoc"><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications-metadata-properties.html" class="awstoc">Metadata Section Properties</a></li></ul></li><li class="awstoc closed"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-example-applications.html" class="awstoc">Example Applications</a><ul class="awstoc"><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-example-ddb.html" class="awstoc">Process DynamoDB Events</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-example-s3.html" class="awstoc">Process Amazon S3 Events</a></li></ul></li><li class="awstoc opened"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-reference.html" class="awstoc">AWS SAM Reference</a><ul class="awstoc opened"><li class="awstoc closed"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html" class="awstoc">Installing the AWS SAM CLI</a><ul class="awstoc"><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-linux.html" class="awstoc">Linux</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-windows.html" class="awstoc">Windows</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-mac.html" class="awstoc">macOS</a></li><li class="awstoc closed"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-additional.html" class="awstoc">Additional Installation Topics</a><ul class="awstoc"><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-linux-path.html" class="awstoc">Adjusting Your Path on Linux</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-windows-path.html" class="awstoc">Adjusting Your Path on Windows</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-mac-path.html" class="awstoc">Adjusting Your Path on macOS</a></li></ul></li></ul></li><li class="awstoc opened"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html" class="awstoc">AWS SAM CLI Command Reference</a><ul class="awstoc opened"><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-build.html" class="awstoc">sam build</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-deploy.html" class="awstoc">sam deploy</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-init.html" class="awstoc">sam init</a></li><li class="awstoc leaf opened"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html" class="awstoc selected opened">sam local generate-event</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-invoke.html" class="awstoc">sam local invoke</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-start-api.html" class="awstoc">sam local start-api</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-start-lambda.html" class="awstoc">sam local start-lambda</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-logs.html" class="awstoc">sam logs</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-package.html" class="awstoc">sam package</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-publish.html" class="awstoc">sam publish</a></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-validate.html" class="awstoc">sam validate</a></li></ul></li></ul></li><li class="awstoc leaf"><a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/doc-history.html" class="awstoc">Document History</a></li></ul></div>
         <div class="ui-resizable-handle ui-resizable-e" style="z-index: 90;"></div></div>
         <div id="main-column" style="margin-left: 350px;">
            <div id="main">
               <div id="main-content">
                  <div id="main-col-body">
                     <table summary="Breadcrumbs">
                        <tbody><tr>
                           <td>
                              <div class="breadcrumb"><a href="https://docs.aws.amazon.com/index.html">AWS Documentation</a> » <a href="https://docs.aws.amazon.com/serverless-application-model/index.html">AWS Serverless Application Model</a> » <a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/index.html">Developer Guide</a> » <a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-reference.html">AWS SAM Reference</a> » <a href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html">AWS SAM CLI Command Reference</a> » <span class="breadcrumb">sam local
                                    generate-event</span></div>
                           </td>
                        </tr>
                     </tbody></table>
                     <div id="language-notice" style="display: none;"><div class="language-notice-icon"></div>
                        <div class="language-notice-text">Currently we are only able to display this content in English.</div>
                     <div class="language-notice-close-btn"></div></div>
                     <div></div>
                     <h1 class="topictitle" id="sam-cli-command-reference-sam-local-generate-event">sam local
                        generate-event
                     </h1>
                     <p>Generates sample payloads from different event sources, such as Amazon S3, Amazon
                        API Gateway, and
                        Amazon SNS. These payloads contain the information that the event sources send to
                        your Lambda
                        functions.
                     </p>
                     <p><b>Usage:</b></p><pre class="programlisting"><div class="code-btn-container"><div class="btn-copy-code" title="Copy"></div><div class="btn-dark-theme" title="Dark theme" title-dark="Dark theme" title-light="Light theme"></div></div><code class="nohighlight hljs">sam local generate-event [OPTIONS] COMMAND [ARGS]...</code></pre><p><b>Examples:</b></p><pre class="programlisting"><div class="code-btn-container"><div class="btn-copy-code" title="Copy"></div><div class="btn-dark-theme" title="Dark theme" title-dark="Dark theme" title-light="Light theme"></div></div><code class="nohighlight hljs">Generate the event that S3 sends to your Lambda function when a new object is uploaded
$ sam local generate-event s3 [put/delete]

You can even customize the event by adding parameter flags. To find which flags apply to your command,
run:

$ sam local generate-event s3 [put/delete] --help

Then you can add in those flags that you wish to customize using

$ sam local generate-event s3 [put/delete] --bucket &lt;bucket&gt; --key &lt;key&gt;

After you generate a sample event, you can use it to test your Lambda function locally
$ sam local generate-event s3 [put/delete] --bucket &lt;bucket&gt; --key &lt;key&gt; | sam local invoke &lt;function logical id&gt;</code></pre><p><b>Options:</b></p>
                     <div class="table">
                        <p class="title"><b></b></p>
                        <div class="table-contents">
                           <table id="w439aac26b9c13c15">

                              <tbody><tr>

                                 <th>Option</th>

                                 <th>Description</th>

                              </tr>


                              <tr>

                                 <td>--help</td>

                                 <td>Shows this message and exits.</td>

                              </tr>

                           </tbody></table>
                        </div>
                     </div>
                     <p><b>Commands:</b></p>
                     <div class="itemizedlist">





















                        <ul class="itemizedlist" type="disc">
                           <li class="listitem">

                              <p>alexa-skills-kit</p>

                           </li>
                           <li class="listitem">

                              <p>alexa-smart-home</p>

                           </li>
                           <li class="listitem">

                              <p>apigateway</p>

                           </li>
                           <li class="listitem">

                              <p>batch</p>

                           </li>
                           <li class="listitem">

                              <p>cloudformation</p>

                           </li>
                           <li class="listitem">

                              <p>cloudfront</p>

                           </li>
                           <li class="listitem">

                              <p>cloudwatch</p>

                           </li>
                           <li class="listitem">

                              <p>codecommit</p>

                           </li>
                           <li class="listitem">

                              <p>codepipeline</p>

                           </li>
                           <li class="listitem">

                              <p>cognito</p>

                           </li>
                           <li class="listitem">

                              <p>config</p>

                           </li>
                           <li class="listitem">

                              <p>dynamodb</p>

                           </li>
                           <li class="listitem">

                              <p>kinesis</p>

                           </li>
                           <li class="listitem">

                              <p>lex</p>

                           </li>
                           <li class="listitem">

                              <p>rekognition</p>

                           </li>
                           <li class="listitem">

                              <p>s3</p>

                           </li>
                           <li class="listitem">

                              <p>ses</p>

                           </li>
                           <li class="listitem">

                              <p>sns</p>

                           </li>
                           <li class="listitem">

                              <p>sqs</p>

                           </li>
                           <li class="listitem">

                              <p>stepfunctions</p>

                           </li>
                        </ul>
                     </div>
                  </div>
                  <noscript>
                     <div>
                        <div>
                           <div>
                              <div id="js_error_message">
                                 <p><img src="https://d1ge0kk1l5kms0.cloudfront.net/images/G/01/webservices/console/warning.png" alt="Warning" /> <strong>Javascript is disabled or is unavailable in your browser.</strong></p>
                                 <p>To use the AWS Documentation, Javascript must be enabled. Please refer to your browser's
                                    Help pages for instructions.
                                 </p>
                              </div>
                           </div>
                        </div>
                     </div>
                  </noscript>
                  <div id="main-col-footer">
                     <div id="doc-conventions"><a target="_top" href="https://docs.aws.amazon.com/general/latest/gr/docconventions.html">Document Conventions</a></div>
                     <div id="next"><a class="awstoc" accesskey="p" href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-init.html">« Previous </a><a class="awstoc" accesskey="n" href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-invoke.html">Next »</a></div>
                     <div id="copyright-main-footer">© 2019, Amazon Web Services, Inc. or its affiliates. All rights reserved.</div>
                  </div>
               </div>
            </div>
            <div id="right-expanded">
               <div id="right-content-wrapper"></div>
            </div>
         </div>
      </div>
      <div id="cookie-notice" style="visibility: hidden;"><div class="cookie-notice-icon"></div>
         <div class="cookie-notice-text">We use cookies to provide and improve our services. By using our site, you consent
            to cookies. <a href="http://aws.amazon.com/legal/cookies">Learn more</a></div>
      <div class="cookie-notice-close-btn"></div></div>
      <div id="footer">
         <div id="footer_short_fb" class="hide" title="Feedback"><a target="_blank" href="https://docs.aws.amazon.com/forms/aws-doc-feedback?hidden_service_name=Serverless%20Application%20Model&amp;topic_url=http://docs.aws.amazon.com/en_us/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html&amp;hidden_guide_name=Developer%20Guide&amp;hidden_api_version=&amp;hidden_file_name=sam-cli-command-reference-sam-local-generate-event"><i class="awsdocs-footer-text fa fa-envelope-o"></i></a></div>
         <div id="footer_toggle" class="mediaobject">
            <div id="footer_toggle_img" class="awsdocs-footer-text fa fa-caret-down"></div>
            <div id="footer_toggle_img_collapse" class="hide awsdocs-footer-text fa fa-caret-right"></div>
         </div>
         <div id="footer-left"><a class="awsdocs-footer-text" target="_top" href="http://aws.amazon.com/terms">Terms of Use</a><span class="awsdocs-footer-text"> | </span><a class="awsdocs-footer-text" target="_top" href="http://aws.amazon.com/privacy">Privacy</a><span class="awsdocs-footer-text"> | </span><span class="awsdocs-footer-text">© 2019, Amazon Web Services, Inc. or its affiliates. All rights reserved.</span></div>
         <div id="footer-right">
            <div id="feedback">
               <div id="forums"></div>
               <div id="feedback-message" class="awsdocs-footer-text">Did this page help you?</div>
               <div id="feedback-yesno-buttons"><a class="awstoc btn btn-default" target="_blank" href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/feedbackyes.html?topic_url=http://docs.aws.amazon.com/en_us/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html">Yes</a><a class="awstoc btn btn-default" target="_blank" href="https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/feedbackno.html?topic_url=http://docs.aws.amazon.com/en_us/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html">No</a></div>
               <div id="feedback-feedback-button"><a class="awstoc btn btn-default" target="_blank" href="https://docs.aws.amazon.com/forms/aws-doc-feedback?hidden_service_name=Serverless%20Application%20Model&amp;topic_url=http://docs.aws.amazon.com/en_us/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-generate-event.html&amp;hidden_guide_name=Developer%20Guide&amp;hidden_api_version=&amp;hidden_file_name=sam-cli-command-reference-sam-local-generate-event">Feedback</a></div>
            </div>
         </div>
      </div>
      <!-- SiteCatalyst code version: H.25.2.
            Copyright 1996-2012 Adobe, Inc. All Rights Reserved
            More info available at http://www.omniture.com --><script language="JavaScript" type="text/javascript" src="./sam local generate-event_files/awshome_s_code.js"></script><script language="JavaScript" type="text/javascript">
         <!--

            // Documentation Service Name
            s.prop66='AWS Serverless Application Model';
            s.eVar66='D=c66';

            // Documentation Guide Name                                                                 
            s.prop65='Developer Guide';
            s.eVar65='D=c65';

            var s_code=s.t();if(s_code)document.write(s_code)//--></script><script language="JavaScript" type="text/javascript">
         <!--
                if(navigator.appVersion.indexOf('MSIE')>=0)document.write(unescape('%3C')+'\!-'+'-')
                //--></script><noscript><img src="https://amazonwebservices.d2.sc.omtrdc.net/b/ss/awsamazondev/1/H.25.2--NS/0" height="1" width="1" border="0" alt="" /></noscript>
      <!--/DO NOT REMOVE/-->
      <!-- End SiteCatalyst code version: H.25.2. -->

<div id="cboxOverlay" style="display: none;"></div><div id="colorbox" class="" role="dialog" tabindex="-1" style="display: none;"><div id="cboxWrapper"><div><div id="cboxTopLeft" style="float: left;"></div><div id="cboxTopCenter" style="float: left;"></div><div id="cboxTopRight" style="float: left;"></div></div><div style="clear: left;"><div id="cboxMiddleLeft" style="float: left;"></div><div id="cboxContent" style="float: left;"><div id="cboxTitle" style="float: left;"></div><div id="cboxCurrent" style="float: left;"></div><button type="button" id="cboxPrevious"></button><button type="button" id="cboxNext"></button><button id="cboxSlideshow"></button><div id="cboxLoadingOverlay" style="float: left;"></div><div id="cboxLoadingGraphic" style="float: left;"></div></div><div id="cboxMiddleRight" style="float: left;"></div></div><div style="clear: left;"><div id="cboxBottomLeft" style="float: left;"></div><div id="cboxBottomCenter" style="float: left;"></div><div id="cboxBottomRight" style="float: left;"></div></div></div><div style="position: absolute; width: 9999px; visibility: hidden; display: none; max-width: none;"></div></div><div class="ui-selectmenu-menu ui-front"><ul aria-hidden="true" aria-labelledby="languageSelection-button" id="languageSelection-menu" role="listbox" tabindex="0" class="ui-menu ui-corner-bottom ui-widget ui-widget-content"></ul></div></body></html>
