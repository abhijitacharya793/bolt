import React from "react";

import {
    Button,
} from "@material-tailwind/react";

import bolt_img from '../../static/img/bolt.jpeg'

import { marked } from "marked";
import "highlight.js/styles/github.css";
import hljs from "highlight.js";
import { useEffect } from "react";

export default function Home() {
    useEffect(() => {
        hljs.highlightAll();
    }, []);

    const markdown = `
  \`\`\`typescript
  Start your journey by executing your first run.
  Our Workflow Library offers a variety
    of ready-to-launch workflows.
  It's designed to help you start quickly
    without the need to build from scratch.
  \`\`\`
`;


    return (
        <>
            <section class="h-screen flex items-center">
                <div class="w-full h-full relative">
                    <img src={bolt_img} alt="Hero" class="absolute inset-0 w-full h-full object-cover rounded-tr-2xl rounded-bl-2xl" />
                    <div class="absolute inset-0 flex items-center justify-center text-center text-white">
                        <div>
                            <code className="font-mono m-6 uppercase bg-gray-900 p-2">Begin Your Automation Journey</code>
                            <div dangerouslySetInnerHTML={{ __html: marked(markdown) }}></div>
                            <form className="mt-8 mb-2 mx-auto w-80 max-w-screen-lg lg:w-1/2">
                                <a href="/scans">
                                    <Button className="mt-6" fullWidth>
                                        Discover Scans
                                    </Button>
                                </a>
                            </form>
                        </div>
                    </div>
                </div>
            </section>
        </>
    )
}
