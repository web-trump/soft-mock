(this["webpackJsonpsoft-mock-template"]=this["webpackJsonpsoft-mock-template"]||[]).push([[42],{439:function(e,t,n){!function(e){"use strict";function t(e){for(var t={},n=e.split(" "),r=0;r<n.length;++r)t[n[r]]=!0;return t}e.defineMode("d",(function(t,n){var r,i=t.indentUnit,o=n.statementIndentUnit||i,a=n.keywords||{},l=n.builtin||{},u=n.blockKeywords||{},s=n.atoms||{},c=n.hooks||{},f=n.multiLineStrings,m=/[+\-*&%=<>!?|\/]/;function d(e,t){var n=e.next();if(c[n]){var i=c[n](e,t);if(!1!==i)return i}if('"'==n||"'"==n||"`"==n)return t.tokenize=p(n),t.tokenize(e,t);if(/[\[\]{}\(\),;\:\.]/.test(n))return r=n,null;if(/\d/.test(n))return e.eatWhile(/[\w\.]/),"number";if("/"==n){if(e.eat("+"))return t.tokenize=y,y(e,t);if(e.eat("*"))return t.tokenize=h,h(e,t);if(e.eat("/"))return e.skipToEnd(),"comment"}if(m.test(n))return e.eatWhile(m),"operator";e.eatWhile(/[\w\$_\xa1-\uffff]/);var o=e.current();return a.propertyIsEnumerable(o)?(u.propertyIsEnumerable(o)&&(r="newstatement"),"keyword"):l.propertyIsEnumerable(o)?(u.propertyIsEnumerable(o)&&(r="newstatement"),"builtin"):s.propertyIsEnumerable(o)?"atom":"variable"}function p(e){return function(t,n){for(var r,i=!1,o=!1;null!=(r=t.next());){if(r==e&&!i){o=!0;break}i=!i&&"\\"==r}return(o||!i&&!f)&&(n.tokenize=null),"string"}}function h(e,t){for(var n,r=!1;n=e.next();){if("/"==n&&r){t.tokenize=null;break}r="*"==n}return"comment"}function y(e,t){for(var n,r=!1;n=e.next();){if("/"==n&&r){t.tokenize=null;break}r="+"==n}return"comment"}function b(e,t,n,r,i){this.indented=e,this.column=t,this.type=n,this.align=r,this.prev=i}function k(e,t,n){var r=e.indented;return e.context&&"statement"==e.context.type&&(r=e.context.indented),e.context=new b(r,t,n,null,e.context)}function v(e){var t=e.context.type;return")"!=t&&"]"!=t&&"}"!=t||(e.indented=e.context.indented),e.context=e.context.prev}return{startState:function(e){return{tokenize:null,context:new b((e||0)-i,0,"top",!1),indented:0,startOfLine:!0}},token:function(e,t){var n=t.context;if(e.sol()&&(null==n.align&&(n.align=!1),t.indented=e.indentation(),t.startOfLine=!0),e.eatSpace())return null;r=null;var i=(t.tokenize||d)(e,t);if("comment"==i||"meta"==i)return i;if(null==n.align&&(n.align=!0),";"!=r&&":"!=r&&","!=r||"statement"!=n.type)if("{"==r)k(t,e.column(),"}");else if("["==r)k(t,e.column(),"]");else if("("==r)k(t,e.column(),")");else if("}"==r){for(;"statement"==n.type;)n=v(t);for("}"==n.type&&(n=v(t));"statement"==n.type;)n=v(t)}else r==n.type?v(t):(("}"==n.type||"top"==n.type)&&";"!=r||"statement"==n.type&&"newstatement"==r)&&k(t,e.column(),"statement");else v(t);return t.startOfLine=!1,i},indent:function(t,n){if(t.tokenize!=d&&null!=t.tokenize)return e.Pass;var r=t.context,a=n&&n.charAt(0);"statement"==r.type&&"}"==a&&(r=r.prev);var l=a==r.type;return"statement"==r.type?r.indented+("{"==a?0:o):r.align?r.column+(l?0:1):r.indented+(l?0:i)},electricChars:"{}",blockCommentStart:"/*",blockCommentEnd:"*/",blockCommentContinue:" * ",lineComment:"//",fold:"brace"}}));var n="body catch class do else enum for foreach foreach_reverse if in interface mixin out scope struct switch try union unittest version while with";e.defineMIME("text/x-d",{name:"d",keywords:t("abstract alias align asm assert auto break case cast cdouble cent cfloat const continue debug default delegate delete deprecated export extern final finally function goto immutable import inout invariant is lazy macro module new nothrow override package pragma private protected public pure ref return shared short static super synchronized template this throw typedef typeid typeof volatile __FILE__ __LINE__ __gshared __traits __vector __parameters "+n),blockKeywords:t(n),builtin:t("bool byte char creal dchar double float idouble ifloat int ireal long real short ubyte ucent uint ulong ushort wchar wstring void size_t sizediff_t"),atoms:t("exit failure success true false null"),hooks:{"@":function(e,t){return e.eatWhile(/[\w\$_]/),"meta"}}})}(n(45))}}]);
//# sourceMappingURL=42.cd994f80.chunk.js.map