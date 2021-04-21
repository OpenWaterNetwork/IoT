(window.webpackJsonp=window.webpackJsonp||[]).push([[32],{103:function(e,t,n){"use strict";n.r(t),n.d(t,"frontMatter",(function(){return a})),n.d(t,"metadata",(function(){return c})),n.d(t,"toc",(function(){return s})),n.d(t,"default",(function(){return d}));var o=n(3),r=n(7),i=(n(0),n(121)),a={sidebar_position:1},c={unversionedId:"thingsboardiotplaftorm/topic1",id:"thingsboardiotplaftorm/topic1",isDocsHomePage:!1,title:"Topic 1",description:"Docusaurus can manage multiple versions of your docs.",source:"@site/docs/thingsboardiotplaftorm/topic1.md",sourceDirName:"thingsboardiotplaftorm",slug:"/thingsboardiotplaftorm/topic1",permalink:"/IoT/docs/thingsboardiotplaftorm/topic1",editUrl:"https://github.com/OpenWaterNetwork/IoT/edit/main/website/docs/thingsboardiotplaftorm/topic1.md",version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"tutorialSidebar",previous:{title:"Sensor node registration on TTN",permalink:"/IoT/docs/buildsensornodes/wseb"},next:{title:"Topic 2",permalink:"/IoT/docs/thingsboardiotplaftorm/topic2"}},s=[{value:"Create a docs version",id:"create-a-docs-version",children:[]},{value:"Add a Version Dropdown",id:"add-a-version-dropdown",children:[]},{value:"Update an existing version",id:"update-an-existing-version",children:[]}],l={toc:s};function d(e){var t=e.components,a=Object(r.a)(e,["components"]);return Object(i.b)("wrapper",Object(o.a)({},l,a,{components:t,mdxType:"MDXLayout"}),Object(i.b)("p",null,"Docusaurus can manage multiple versions of your docs."),Object(i.b)("h2",{id:"create-a-docs-version"},"Create a docs version"),Object(i.b)("p",null,"Release a version 1.0 of your project:"),Object(i.b)("pre",null,Object(i.b)("code",{parentName:"pre",className:"language-bash"},"npm run docusaurus docs:version 1.0\n")),Object(i.b)("p",null,"The ",Object(i.b)("inlineCode",{parentName:"p"},"docs")," folder is copied into ",Object(i.b)("inlineCode",{parentName:"p"},"versioned_docs/version-1.0")," and ",Object(i.b)("inlineCode",{parentName:"p"},"versions.json")," is created."),Object(i.b)("p",null,"Your docs now have 2 versions:"),Object(i.b)("ul",null,Object(i.b)("li",{parentName:"ul"},Object(i.b)("inlineCode",{parentName:"li"},"1.0")," at ",Object(i.b)("inlineCode",{parentName:"li"},"http://localhost:3000/docs/")," for the version 1.0 docs"),Object(i.b)("li",{parentName:"ul"},Object(i.b)("inlineCode",{parentName:"li"},"current")," at ",Object(i.b)("inlineCode",{parentName:"li"},"http://localhost:3000/docs/next/")," for the ",Object(i.b)("strong",{parentName:"li"},"upcoming, unreleased docs"))),Object(i.b)("h2",{id:"add-a-version-dropdown"},"Add a Version Dropdown"),Object(i.b)("p",null,"To navigate seamlessly across versions, add a version dropdown."),Object(i.b)("p",null,"Modify the ",Object(i.b)("inlineCode",{parentName:"p"},"docusaurus.config.js")," file:"),Object(i.b)("pre",null,Object(i.b)("code",{parentName:"pre",className:"language-js",metastring:'title="docusaurus.config.js"',title:'"docusaurus.config.js"'},"module.exports = {\n  themeConfig: {\n    navbar: {\n      items: [\n        // highlight-start\n        {\n          type: 'docsVersionDropdown',\n        },\n        // highlight-end\n      ],\n    },\n  },\n};\n")),Object(i.b)("p",null,"The docs version dropdown appears in your navbar:"),Object(i.b)("p",null,Object(i.b)("img",{alt:"Docs Version Dropdown",src:n(129).default})),Object(i.b)("h2",{id:"update-an-existing-version"},"Update an existing version"),Object(i.b)("p",null,"It is possible to edit versioned docs in their respective folder:"),Object(i.b)("ul",null,Object(i.b)("li",{parentName:"ul"},Object(i.b)("inlineCode",{parentName:"li"},"versioned_docs/version-1.0/hello.md")," updates ",Object(i.b)("inlineCode",{parentName:"li"},"http://localhost:3000/docs/hello")),Object(i.b)("li",{parentName:"ul"},Object(i.b)("inlineCode",{parentName:"li"},"docs/hello.md")," updates ",Object(i.b)("inlineCode",{parentName:"li"},"http://localhost:3000/docs/next/hello"))))}d.isMDXComponent=!0},121:function(e,t,n){"use strict";n.d(t,"a",(function(){return p})),n.d(t,"b",(function(){return m}));var o=n(0),r=n.n(o);function i(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function a(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,o)}return n}function c(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?a(Object(n),!0).forEach((function(t){i(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):a(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,o,r=function(e,t){if(null==e)return{};var n,o,r={},i=Object.keys(e);for(o=0;o<i.length;o++)n=i[o],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(o=0;o<i.length;o++)n=i[o],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var l=r.a.createContext({}),d=function(e){var t=r.a.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):c(c({},t),e)),n},p=function(e){var t=d(e.components);return r.a.createElement(l.Provider,{value:t},e.children)},u={inlineCode:"code",wrapper:function(e){var t=e.children;return r.a.createElement(r.a.Fragment,{},t)}},b=r.a.forwardRef((function(e,t){var n=e.components,o=e.mdxType,i=e.originalType,a=e.parentName,l=s(e,["components","mdxType","originalType","parentName"]),p=d(n),b=o,m=p["".concat(a,".").concat(b)]||p[b]||u[b]||i;return n?r.a.createElement(m,c(c({ref:t},l),{},{components:n})):r.a.createElement(m,c({ref:t},l))}));function m(e,t){var n=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var i=n.length,a=new Array(i);a[0]=b;var c={};for(var s in t)hasOwnProperty.call(t,s)&&(c[s]=t[s]);c.originalType=e,c.mdxType="string"==typeof e?e:o,a[1]=c;for(var l=2;l<i;l++)a[l]=n[l];return r.a.createElement.apply(null,a)}return r.a.createElement.apply(null,n)}b.displayName="MDXCreateElement"},129:function(e,t,n){"use strict";n.r(t),t.default=n.p+"assets/images/docsVersionDropdown-dda80f009a926fb2dd92bab8faa6c4d8.png"}}]);