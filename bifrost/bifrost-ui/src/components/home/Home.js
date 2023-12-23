import React from "react";

import {
    Card,
    Input,
    Checkbox,
    Button,
    Typography,
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
            <section className="flex pt-10">
                <div className="relative flex items-center justify-center">
                    <div className="w-full h-full hidden lg:block m-8 opacity-70">
                        <img
                            src={bolt_img}
                            className="h-3/4 w-full object-cover rounded-3xl"
                        />
                    </div>
                    <div className="absolute top-1/4 right-1/3 container px-10 w-2/5 flex flex-col items-center justify-center p-8">
                        <div className="text-right">
                            <code className="font-mono m-6 uppercase bg-red-50 p-2">Begin Your Automation Journey</code>
                            <div dangerouslySetInnerHTML={{ __html: marked(markdown) }}></div>
                        </div>
                        <form className="mt-8 mb-2 mx-auto w-80 max-w-screen-lg lg:w-1/2">
                            <a href="/scans">
                                <Button className="mt-6" fullWidth>
                                    Discover Scans
                                </Button>
                            </a>
                        </form>
                    </div>
                </div>
            </section>
        </>
    )
}
